#!/bin/bash

#Create control fastq folder and move reads
cd /home/lab/tbCDC/reads/$1
mkdir control_fastqs
mv CON* control_fastqs

cd /home/lab/tbCDC/varpipe_wgs/data
bash /home/lab/sra_sub/submit_to_SRA.sh $1

#Must manually upload demo file

cd /home/lab/sra_sub
python3 SRA_sub.py prep_SRA_submission "$1"


