#!/bin/bash

#This script creates the custom outputs that AMD requires: 1) interpretations of the variant and 2) stats on all the samples including pass/fail. All this information is pulled from the CDC varpipeline and parsed into csvs. 
reads="/home/lab/tbCDC/reads"
work_dir="/home/lab/tbCDC/varpipe_wgs/data"


cd Output/$1
echo "Sample\tINH\tRIF\tPZA\tFQ\tEMB" > $1\_all_interpretations.tsv
#parsing the variant interpretations for each sample into the interpretations tsv

echo "Sample ID\tSample Name\tPercent Reads Mapped\tAverage Genome Coverage Depth\tPercent Reference Genome Covered\tCoverage Drop\tPipeline Version\tDate\tPass/Fail\tClassification\tClassification Abundance" > $1\_all_stats.tsv
#parsing the stats for each sample into the stats tsv. Uses the individual stats file and kraken file generated for each sample and compile
for i in */; do
	dir=${i%/}
	if [ "$dir" = "QC" ]; then
		for j in $i/*/; do
			#echo $j
			cp $j/*_stats.txt .
			cp $j/*_kraken.txt .

		done
	else
		#echo $dir
		python $work_dir/output_scripts/create_resistance_table.py $dir/$dir\_interpretation.txt >> $1\_all_interpretations.tsv
		cp $dir/$dir\_stats.txt .
		cp $dir/$dir\_kraken.txt .
	fi
done       

for i in *_stats.txt; do
	sample=${i%_*}
	#echo $sample
	python $work_dir/output_scripts/get_stats.py $sample\_stats.txt $sample\_kraken.txt >> $1\_all_stats.tsv;
done
#rm *_stats.txt
#rm *_kraken.txt

#creating excel versions
python $work_dir/output_scripts/convert_tsv_xlsx.py $1\_all_stats.tsv
python $work_dir/output_scripts/convert_tsv_xlsx.py $1\_all_interpretations.tsv
cd $work_dir
