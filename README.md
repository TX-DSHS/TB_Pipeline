# TB_Pipeline

Utilizing CDC Varpipe_wgs 1.0.2- This is a bioinformatic pipeline developed to analyze Mycobacterium tuberculosis whole genome sequencing (WGS) data generated on Illumina NGS platforms. The pipeline incorporates several open-sourced tools and custom python scripts to accept fastq files, map the reads against Mycobacterium tuberculosis H37Rv (NC_000962.3) reference genome, identify variants in the sample genome and provide a coverage report (list of tools and custom scripts in Supplementary tables 1 & 4). The results are reported in the standard variant call file (VCF) format as well as a printable PDF file format. Source code from CDC can be found here: ( https://github.com/CDCgov/NCHHSTP-DTBE-Varpipe-WGS)


**Dependencies**

Bcftools 1.11

BEDTools 2.17

BWA 0.7.17

GATK 4.1.6.0

Piccard Tools 2.23.8

Python 2.7.5

Java 1.8.0_131

Samtools 1.11

snpEff 4.3

Trimmomatic 0.39


**Install Instructions**

The TB pipeline requires a combination of github code and AWS S3 stored databases and tools to run. Follow these instructions to pull all materials and set up the dependencies:

1. Clone this repository to a /bioinformatics/ section of the AWS EC2 with the command: 

git clone  https://github.com/TX-DSHS/tbCDC.git

2. Run the command "bash setup.sh" to finish the installation. This script runs several steps: Downloads the clockwork singularity image, Downloads GATK, Builds a reference fasta and creates BWA indexes
3. Create the conda environment using the requirements file with this command: conda create --name tbCDC --file requirements.txt
4. Edit the /tools/clockwork-0.11.3/clockwork script with the right local filepath
5. Add the path in 2 above to your shell path before running the pipeline
6. Pull the kraken database from AWS S3 to /bioinformatics/varpipe_wgs/data/kraken2_db with the command: 

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/kraken2_db/ /bioinformatics/varpipe_wgs/data/kraken2_db/ --region us-gov-west-1

7. Pull the tools/ folders from AWS S3 to /bioinformatics/varpipe_wgs/tools/ with the commands: 

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/clockwork-0.11.3/ /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/bcftools /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/gatk-4.2.4.0 /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/snpEff /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/bwa /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/picard.jar /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/ref2.fa /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1

aws s3 cp --recursive s3://804609861260-bioinformatics-infectious-disease/TB/TB_Pipeline/tools/samtools /bioinformatics/varpipe_wgs/tools/ --region us-gov-west-1






**Run Command**

Within in the /bioinformatics/.../data directory, run this command:
/runVarpipeline.sh TX-########


The pipeline will take several hours to complete. Output folder will be zipped upon completion.
For post processing, run this command:
bash post_proc.sh TX-#########



**Disclaimer** 

The Laboratory Branch (LB) of the Division of Tuberculosis Elimination developed this bioinformatic pipeline for analyzing whole genome sequencing data generated on Illumina platforms. This is not a controlled document. The performance characteristics as generated at Centers for Disease Control and Prevention (CDC) are specific to the version as written. These documents are provided by LB solely as an example for how this test performed within LB.  The recipient testing laboratory is responsible for generating validation or verification data as applicable to establish performance characteristics as required by the testing laboratory’s policies, applicable regulations, and quality system standards. These data are only for the sample and specimen types and conditions described in this procedure. Tests or protocols may include hazardous reagents or biological agents. No indemnification for any loss, claim, damage, or liability is provided for the party receiving an assay or protocol. Use of trade names and commercial sources are for identification only and do not constitute endorsement by the Public Health Service, the United States Department of Health and Human Services, or the Centers for Disease Control and Prevention

# TB_varpipe
# TB_varpipe
