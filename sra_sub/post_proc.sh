#!/bin/bash
aws_bucket="s3://804609861260-bioinformatics-infectious-disease"
reads="/home/lab/tbCDC/reads"
work_dir="/home/lab/tbCDC/varpipe_wgs/data"
sra_sub="/home/lab/sra_sub"


#Create control fastq folder and move reads
cd $reads/$1
mkdir control_fastqs
mv CON* control_fastqs

cd $work_dir
bash $sra_sub/submit_to_SRA.sh $1

#Must manually upload demo file

cd $sra_sub
python3 SRA_sub.py prep_SRA_submission "$1"


