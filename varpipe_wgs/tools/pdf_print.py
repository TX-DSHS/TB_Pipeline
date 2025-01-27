""" Accepts summary text file and prints out PDF report """

from fpdf import FPDF
import csv
from string import join
import sys
import pandas

#Attempt to read in the demo file. delete here to end if unsuccessful
#rows=[]
#with open("/home/lab/tbCDC/varpipe_wgs/data/TX-VH00729-231030A_demo.csv", 'r') as file:
  #reader=csv.DictReader(file)
  #for row in reader: 
    #rows.append(row)

#csvFile = pandas.read_csv('/home/lab/tbCDC/varpipe_wgs/data/TX-VH00729-231030A_demo.csv')
#print(csvFile['PatientSex'])
 


class PDF(FPDF):
    def header(self):
        input1 = sys.argv[1]
        f = open(input1, "r")
        f_reader = csv.reader(f, delimiter='\t')
        k = []
        for z in f_reader:
            x = '\t'.join(z)
            if len(z) > 0 and 'Sample Summary' not in x and 'Date' not in x:
               k.append(z)
            if 'Date' in x:
               k.append(z)
               break
        self.set_font('Arial', '', 20)
        self.cell(30, 5, str("Next-Generation Sequencing (NGS) Analysis Report for Mycobacterium tuberculosis"), border=0)
        self.ln(10.0)
        #self.cell(250,10,"TEXAS DEPARTMENT OF STATE HEALTH SERVICES")
        self.image("/home/klong/dshs_tb/cdc/varpipe_wgs/tools/DSHS-standard-color-print.jpg",h=15,w=100)
        self.set_font('Arial', '', 9)
        self.ln(7.0)
        for r in k:
            for d in r:
                self.cell(30, 5, str(d), border=0)
            self.ln(5)
        f.close()
        # Line break
        self.ln(10)


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        if int(self.page_no()) == 1:
            disclaimer = "DISCLAIMER: The presence of a gene variant does not necessarily indicate that the isolate is resistant to the corresponding drug. As such, test results are not diagnostic and should be interpreted in the context of clinical findings and other laboratory data. Drug susceptibility variant interpretation (S= susceptible, U=undetermined, R= resistant) is based on data from the World Health Organization (WHO) catalogue of Mtb complex mutations. Microorganism identification was performed by analyzing its whole genome using Next-Generation Sequencing (NGS). The test and its performance characteristics were developed and determined by the Texas Department of State Health Services Laboratory. This test has not been approved or cleared by the U.S. Food and Drug Administration. The Varpipe_wgs pipeline was developed at Centers for Disease Control and Prevention (CDC) to analyze whole genome sequencing (WGS) data of Mycobacterium tuberculosis (Mtb) on Illumina NGS platforms. Sequence reads are mapped to the Mtb (NC_000962.3) H37Rv reference genome. This pipeline uses open source and custom tools for bioinformatics analysis. For questions about this report, please contact WGS.DSHS@dshs.texas.gov."
            self.set_y(-40)
            pdf.multi_cell(270,5,str(disclaimer), border=0)
            self.set_y(-10)
            self.cell(0, 10, 'Page ' + str(self.page_no()) + ' of {nb}', 0, 0, 'C')
        else:
            self.cell(0, 10, 'Page ' + str(self.page_no()) + ' of {nb}', 0, 0, 'C')



pdf = PDF('L', 'mm', 'A4')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', '', 10)

input1 = sys.argv[1]
input2 = sys.argv[2]

f2 = open(input1, 'r')
f2_reader = csv.reader(f2, delimiter='\t')
p = []
for x in f2_reader:
    y = '\t'.join(x)
    if 'Sample Name' in y or  'Drop' in y or 'Pipeline' in y or 'Date' in y:
       continue
    if 'Variant' in y:
       break
       #Labware Attempt
    #if 'Sample Name' in y and 'Sample Name'==csvFile['HAI_WGS_ID(YYYYCB-#####)']:
       #labware_id=csvFile['KEY']
       #pdf.cell(0,5,labware_id,0,1)
               #end
    if 'Target' in y:
       pdf.set_font('Arial', 'B', 9)
       pdf.cell(0, 5, y, 0, 1)
       pdf.set_font('Arial', '', 9)   
    
    elif len(x) > 0:
       p.append(x)
      
f2.close()

pdf.ln(20)
f4 = open(input1, 'r')
f4_reader = csv.reader(f4, delimiter='\t')
q = []
pdf.set_font('Arial', 'B', 9)
pdf.cell(0, 5, 'Interpretations Summary:', 0, 1)
lines = False
for z in f4_reader:
    w = '\t'.join(z)
    if 'Interpretations' in w:
       lines = True
       continue
    if lines == True and len(w) > 0:
       q.append(z)
f4.close()

pdf.set_font('Arial', '', 9)
pdf.ln(0.5)
for row in q:
    for datum in row:
       if len(datum) > 70:
          datum = datum[:69] + '*'
       pdf.cell(120, 5, str(datum), border=0)
    pdf.ln(5)

pdf.output(input2, 'F')
