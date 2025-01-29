aws_bucket="s3://804609861260-bioinformatics-infectious-disease"
reads="/home/lab/tbCDC/reads"
work_dir="/home/lab/tbCDC/varpipe_wgs/data"

/home/dnalab/.aspera/connect/bin/ascp -i /home/dnalab/aspera.openssh -QT -l100m -k1 -d $reads/$1/ subasp@upload.ncbi.nlm.nih.gov:uploads/lab.microbiology_dshs.state.tx.us_rJiZeQDA/$1
