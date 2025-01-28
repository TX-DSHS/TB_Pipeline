#!/bin/bash

run_name=$1

mkdir /home/lab/sra_sub_test/$1_SRA_files
mv /home/lab/sra_sub_test/$1_SRA_metadata.tsv /home/lab/sra_sub_test/$1_SRA_attribute.tsv /home/lab/sra_sub_test/$1_SRA_files
aws s3 cp --recursive /home/lab/sra_sub_test/$1_SRA_files s3://804609861260-bioinformatics-infectious-disease/TB/ANALYSIS_RESULTS/$1_SRA_files --region us-gov-west-1
aws s3 cp --recursive /home/lab/sra_sub_test/$1_SRA_attribute.tsv s3://804609861260-bioinformatics-infectious-disease/TB/ANALYSIS_RESULTS/$1_SRA_files --region us-gov-west-1
cp /home/lab/sra_sub_test/$1_SRA_metadata.tsv  /home/lab/tbCDC/varpipe_wgs/data/Output/
cp /home/lab/sra_sub_test/$1_SRA_attribute.tsv /home/lab/tbCDC/varpipe_wgs/data/Output/

