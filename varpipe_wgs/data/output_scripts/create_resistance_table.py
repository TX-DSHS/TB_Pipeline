import sys

#print("Sample\tINH\tRIF\tPZA\tFQ\tEMB")
out=""
for line in open(sys.argv[1]):
    if not line.startswith("Sample ID\t"):
        sample = line.split("\t")[0]
        out = out + line.split("\t")[3].strip() + "\t"
print(sample + "\t" + out.strip())
