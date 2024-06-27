#!/usr/bin/env python3
print("beginning script")

import sys
import openpyxl
import shutil
import xlrd
import pandas as pd
from zipfile import ZipFile
from glob import glob
from os import path
from datetime import date
print("importing complete")


def prep_SRA_submission(run_name):


    filename = "/home/lab/tbCDC/varpipe_wgs/data/Output/{}.zip".format(run_name)
    extract_dir = "/home/lab/sra_sub/output_files"
    archive_format = "zip"
    shutil.unpack_archive(filename, extract_dir, archive_format) 
    print("zip file unpacked successfully.")
   
    results = pd.read_csv("/home/lab/sra_sub/output_files/{}/{}_all_stats.tsv".format(run_name,run_name), sep="\t", header=0, index_col=None)
    
    results["Untrimmed Sample ID"]=results["Sample ID"].apply(str)
    results = results.astype({"Untrimmed Sample ID": str})
    sample_id=results["Untrimmed Sample ID"]  
    print(sample_id)
    
    results["Sample ID"] = results["Sample ID"].str.split('-').str[:4].str.join('-')
    results=results[~results["Sample ID"].str.contains("CON")]
    
    print("stats ready")
    print(results)
      
    reads_dir = "/home/lab/tbCDC/reads/{}/".format(run_name)
    print("reads dir ready")
    
    metadata = pd.read_csv("/home/lab/sra_sub/templates/SRA_metadata_template.txt", sep="\t", header=0, index_col=None)
    print("metadata template ready")
    
    attribute = pd.read_csv("/home/lab/sra_sub/templates/attribute_template.txt", sep="\t", header=0, index_col=None)
    print("attribute template ready")


#    if glob("/home/lab/sra_sub/{}*.xlsx".format(run_name)):
#        try:
    demofile = glob("/home/lab/sra_sub/demo_files/{}*.xlsx".format(run_name))[0]
    demo = pd.read_excel(demofile, engine="openpyxl")
    demo['IsolatDate'] = pd.to_datetime(demo['IsolatDate'])
    demo['IsolatDate'] = demo['IsolatDate'].dt.date
    print("demo ready")
    print(demo)

    results = pd.merge(results, demo, left_on = "Sample ID", right_on = "TB_WGS_ID(TX-DSHS-MTB-YY#####)", how = "outer")
    results.fillna('missing', inplace=True)
    print(results)
    #results.to_csv(results+"_printed.tsv", sep="\t", index = False)
 #       except:
 ###          results["SourceSite"] = "missing"
 #          results["Submitter"] = "missing"
 #          results["KEY"] = "missing"
 #   else:
 #      results["SourceSite"] = "missing"
 #      results["Submitter"] = "missing"
 #      results["KEY"] = "missing"
    control_string="CON"
    control_string_2="ATC"
    
    #results=results[control_string or control_string_2 not in results["Sample Name"]]
    #results=results[results["Sample Name"]!="PositiveControl"]
    #results=results[results["Sample Name"]!="missing"]
    print(results)
    results.sort_values(by="Sample ID", ascending=True, inplace=True)
    instrument = run_name.split("-")[1]

    if instrument[0] == "M":
        instrument_name = "Illumina MiSeq"
    elif instrument[0] == "V":
        instrument_name = "Nextseq 2000"
    print(instrument_name)

    #control_string="CON"
    #control_string_2="ATC"
#attempting to trim sample name    
    for i, row in results.iterrows():
        if (control_string or control_string_2 not in row["Sample Name"]) and row["Sample Name"]!="missing" and row["Percent Reads Mapped"]>=90 and row["Average Genome Coverage Depth"]>=50 and row["Percent Reference Genome Covered"]>=90:
          sample_id=row["Untrimmed Sample ID"]
          sample_id=str(sample_id)
          trimmed_sample_id=row["Sample ID"]
          date=row["IsolatDate"]
          loc_country=row["SourceCountry"]
          loc_state=row["SourceState"]
          #parts = sample_id.split("_")
          #trimmed_sample_id ="_".join(parts[:3])
          sourceSite = row["SourceSite"]
          submitter = row["Submitter"]
          age=row["PatientAgeYears"]
          print(age)
            #print(sourceSite, submitter)
          fastq_files = []
          sample_id=str(sample_id)
          fastqs = reads_dir + sample_id + "*"
          fastqs=str(fastqs)
          print(fastqs)
          for fastq in glob(fastqs):
            fastq_files.append(path.basename(fastq))
          print(fastq_files)
          #print(fastq_files[0])
          new_row_metadata = {"sample_name": trimmed_sample_id, "library_ID": trimmed_sample_id, "title": "Illumina sequencing of {}".format(trimmed_sample_id),
               "library_strategy": "WGS", "library_source": "GENOMIC",  "library_selection": "RANDOM", "library_layout": "PAIRED",
               "platform": "ILLUMINA",  "instrument_model": instrument_name, "design_description": "Illumina DNA Prep", "filetype": "fastq",
               "filename": fastq_files[0], "filename2": fastq_files[1], "filename3": "", "filename4": "",  "assembly": "", "fasta_file": ""}
          metadata = metadata.append(new_row_metadata, ignore_index = True)
          
          org_wr=row["Classification"]
          org=org_wr.replace('complex','')
          new_row_attr = {"*sample_name": trimmed_sample_id, "sample_title": "missing", "bioproject_accession": "PRJNA1080563", "*organism": org,"strain": "missing", "*isolate": "Whole Organism", "*collected_by": "Texas Department of State Health Services", "*collection_date": date, "*geo_loc_name": loc_country+":"+loc_state,  "*isolation_source": sourceSite, "*lat_lon": "missing", "culture_collection": "missing", "genotype": "missing", "*host":"Homo sapiens", "host_age": age, "host_description":" missing", "*host_disease": "Tuberculosis"}
          
          attribute = attribute.append(new_row_attr, ignore_index = True)
    metadata.to_csv(run_name + "_SRA_metadata.tsv", sep = "\t", index = False)
    attribute.to_csv(run_name + "_SRA_attribute.tsv", sep = "\t", index = False)
    


 
    return results

   
if __name__ == "__main__":
    globals()[sys.argv[1]](sys.argv[2])
