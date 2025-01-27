#!/bin/bash


aws_bucket="s3://804609861260-bioinformatics-infectious-disease"
reads="/home/lab/tbCDC/reads"
work_dir="/home/lab/tbCDC/varpipe_wgs/data"

#conda setup
cd $work_dir
source /home/lab/miniconda3/etc/profile.d/conda.sh 
conda activate tbCDC

#make output dir
rm -rf $reads/$1 $work_dir/Output/$1.zip $work_dir/Output/$1
rm -r $reads/T*
rm -r $work_dir/Output/*
project=$1
proj_dir=$work_dir/Output/$1
mkdir -p $proj_dir

#get files from aws, create file links
aws s3 cp $aws_bucket/TB/RAW_RUNS/$1\.zip $reads/$1\.zip --region us-gov-west-1
unzip $reads/$1\.zip -d $reads
rm -rf $reads/$1\.zip
ln -sf $reads/$1/*.fastq.gz $proj_dir
rm -rf $proj_dir/Undetermined*


#create script to run all samples
#miseq runs have the L001, nextseq runs do not have the L001
if [[ "$1" == *"VH"* ]]; then 
	ls $proj_dir/*_R1_001.fastq.gz | sed 's/_R1_001.fastq.gz//g' | cut -d "/" -f9 | awk '{print "../tools/Varpipeline -q '"$proj_dir"'/"$0"_R1_001.fastq.gz -r ../tools/ref2.fa -p '"$project"' -n "$0" -q2 '"$proj_dir"'/"$0"_R2_001.fastq.gz -a -v"}' > tbCDC.sh
else 
	ls $proj_dir/*_L001_R1_001.fastq.gz | sed 's/_L001_R1_001.fastq.gz//g' | cut -d "/" -f9 | awk '{print "../tools/Varpipeline -q '"$proj_dir"'/"$0"_L001_R1_001.fastq.gz -r ../tools/ref2.fa -p '"$project"' -n "$0" -q2 '"$proj_dir"'/"$0"_L001_R2_001.fastq.gz -a -v"}' > tbCDC.sh
fi

#cleanup
echo "rm -f $proj_dir/*.fastq.gz" >> tbCDC.sh

#create extra outputs
echo "sh $work_dir/output_scripts/run_kraken.sh $1" >> tbCDC.sh
echo "sh $work_dir/output_scripts/create_outputs.sh $1" >> tbCDC.sh
echo "rm -rf $proj_dir/*/trimmomatic && rm -rf $proj_dir/QC/*/trimmomatic" >> tbCDC.sh
echo "cd $work_dir/Output/ && zip -r $1.zip $1 && rm -rf $1 && cd $work_dir" >> tbCDC.sh
echo "aws s3 cp $work_dir/Output/$1.zip $aws_bucket/TB/ANALYSIS_RESULTS/$1.zip" >> tbCDC.sh

#finish message
echo "echo 'Pipeline complete!'" >> tbCDC.sh

#run
echo "Starting Pipeline!"
nohup bash tbCDC.sh & disown
