# TB_pipeline

Utilizing CDC Varpipe_wgs 1.0.2- This is a bioinformatic pipeline developed to analyze Mycobacterium tuberculosis whole genome sequencing (WGS) data generated on Illumina NGS platforms. The pipeline incorporates several open-sourced tools and custom python scripts to accept fastq files, map the reads against Mycobacterium tuberculosis H37Rv (NC_000962.3) reference genome, identify variants in the sample genome and provide a coverage report (list of tools and custom scripts in Supplementary tables 1 & 4). The results are reported in the standard variant call file (VCF) format as well as a printable PDF file format. Source code from CDC can be found here: (https://github.com/CDCgov/NCHHSTP-DTBE-Varpipe-WGS)

![TB_workflow](https://github.com/TX-DSHS/tbCDC/blob/cf3d4f034305ccf411376789165b689bf515fe4a/TB%20Pipeline.pdf)

# Prerequisites
To run the pipeline locally, you will need to have the following programs installed:

Python 2.7,
Python 3,
Java 1.8,
Singularity >=3.5

The remaining programs used by the pipeline are included in this repository in the tools/ directory.

# Installation Instructions:
1. Clone the CDC official repository to the /bioinformatics/ section of the AWS EC2 with the command:
git clone https://github.com/CDCGov/NCHHSTP-DTBE-Varpipe-WGS.git
2. Run setup.sh to finish the installation. This script runs several steps:
Downloads the clockwork singularity image
Downloads GATK
Builds a reference fasta and creates BWA indexes
3. Clone this repository to a separation /bioinformatics/ section of the AWS EC2 for post processing with the command: git clone https://github.com/TX-DSHS/tbCDC.git
4. Create the conda environment using the requirements file with this command: conda create --name tbCDC --file requirements.txt

# Commands:
Within in the /bioinformatics/.../data directory, run this command:
/runVarpipeline.sh TX-########

The pipeline will take several hours to complete. Output folder will be zipped upon completion. 

For post processing, within the /bioinformatics/..../sra_sub directory, run this command: 
bash post_proc.sh TX-#########


