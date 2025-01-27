import sys
import pandas as pd

kraken_list = []
for line in open(sys.argv[2]):
    classify = line.split("\t")
    if classify[3] == "G1" or classify[3] == "S":
        #classification = classify[5].strip()
        #perc = classify[0].strip()
        #print(classification)
        #print(perc)
        #break
        kraken_list.append(classify)
df1 = pd.DataFrame(kraken_list, columns=['% of Reads', 'Total Reads', 'Specific_Reads', 'Level', 'TaxID', 'Name'])
df1.Specific_Reads = df1.Specific_Reads.astype(int)
df1 = df1.sort_values(by=['Specific_Reads'], ascending=False).reset_index(drop=True)
call = df1.iat[0, 5]
perc = df1.iat[0, 0]
classification = call.strip()


pass_fail = ""
for line in open(sys.argv[1]):
    pass_fail = ""
    if not line.startswith("Sample ID\t"):
        fields = line.split("\t")
        if float(fields[2]) < 90.0:
            pass_fail = "FAIL (Percent Reads Mapped < 90%)"
        elif int(fields[3]) < 50:
            pass_fail = "FAIL (Average Genome Coverage Depth < 50x)"
        elif float(fields[4]) < 90.0:
            pass_fail = "FAIL (Percent Reference Genome Covered < 90%)"
        else:
            pass_fail = "PASS"
        print(line.strip() + "\t" + pass_fail + "\t" + classification + "\t" + perc)
