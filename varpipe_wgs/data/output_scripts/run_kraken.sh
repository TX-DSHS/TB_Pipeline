#!/bin/bash

#This script runs kraken to classify the samples for AMD. 
reads="/home/lab/tbCDC/reads"
work_dir="/home/lab/tbCDC/varpipe_wgs/data"

cd Output/$1
for i in */; do
        dir=${i%/}
        if [ "$dir" = "QC" ]; then
		cd QC
		for j in */; do
			dir=${j%/}
			docker run -v $work_dir/:/data/ staphb/kraken2 kraken2 --paired --threads 8 --db kraken2_db /data/Output/$1/QC/$dir/trimmomatic/$dir\_paired_1.fastq.gz /data/Output/$1/QC/$dir/trimmomatic/$dir\_paired_2.fastq.gz --output - --report /data/Output/$1/QC/$dir/$dir\_kraken.txt --gzip-compressed
                done
        else
		docker run -v $work_dir/:/data/ staphb/kraken2 kraken2 --paired --threads 8 --db kraken2_db /data/Output/$1/$dir/trimmomatic/$dir\_paired_1.fastq.gz /data/Output/$1/$dir/trimmomatic/$dir\_paired_2.fastq.gz --output - --report /data/Output/$1/$dir/$dir\_kraken.txt --gzip-compressed
        fi
done

