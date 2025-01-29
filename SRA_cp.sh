#!/bin/bash

run_name=$1
aws_bucket="s3://804609861260-bioinformatics-infectious-disease"
reads="/home/lab/tbCDC/reads"
work_dir="/home/lab/tbCDC/varpipe_wgs/data"
sra_sub_test="/home/lab/sra_sub_test"


mkdir $sra_sub_test/$1_SRA_files
mv $sra_sub_test/$1_SRA_metadata.tsv $sra_sub_test/$1_SRA_attribute.tsv $sra_sub_test/$1_SRA_files
aws s3 cp --recursive $sra_sub_test/$1_SRA_files s3://804609861260-bioinformatics-infectious-disease/TB/ANALYSIS_RESULTS/$1_SRA_files --region us-gov-west-1
aws s3 cp --recursive $sra_sub_test/$1_SRA_attribute.tsv s3://804609861260-bioinformatics-infectious-disease/TB/ANALYSIS_RESULTS/$1_SRA_files --region us-gov-west-1
cp $sra_sub_test/$1_SRA_metadata.tsv  $work_dir/Output/
cp $sra_sub_test/$1_SRA_attribute.tsv $work_dir/Output/

