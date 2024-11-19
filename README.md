# TB_pipeline

Utilizing CDC Varpipe_wgs 1.0.2- This is a bioinformatic pipeline developed to analyze Mycobacterium tuberculosis whole genome sequencing (WGS) data generated on Illumina NGS platforms. The pipeline incorporates several open-sourced tools and custom python scripts to accept fastq files, map the reads against Mycobacterium tuberculosis H37Rv (NC_000962.3) reference genome, identify variants in the sample genome and provide a coverage report (list of tools and custom scripts in Supplementary tables 1 & 4). The results are reported in the standard variant call file (VCF) format as well as a printable PDF file format. Source code from CDC can be found here: (https://github.com/CDCgov/NCHHSTP-DTBE-Varpipe-WGS)

![TB_workflow](https://github.com/TX-DSHS/tbCDC/blob/cf3d4f034305ccf411376789165b689bf515fe4a/TB%20Pipeline.pdf)

Install:
Download TB pipeline from (https://github.com/TX-DSHS/tbCDC.git) to the /bioinformatics/ proper directory of AWS EC2: 
    git clone https://github.com/TX-DSHS/tbCDC.git

Command:
/runVarpipeline.sh TX-########


