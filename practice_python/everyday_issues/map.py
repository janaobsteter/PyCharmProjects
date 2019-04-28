import os

os.chdir("/home/jana/novigen/")
finrep = "Final_Report.txt"

[en for en, a in enumerate(open(finrep))]

for en,a in enumerate(open(finrep)):
    ## Header of the Illumina row format (line below the [Data] line)
    if 'Allele1' in a:
        readfrom=True
        line=a.lower().strip().split("\t")
        if not 'allele1 - '+allele.lower() in line:
            print("ERROR: The header does not contain the required field: Allele1 - "+allele)
            print("Header read:")
            print("Possible causes:")
            print("The header in the Illumina header has changed (no 'Allele1 - '"+allele+" field is present - not case sensitive!)")
            print("SOLUTION: Contact ezequiel.nicolazzi@ptp.it, or if you know how to code in python, change the if string related to this")
            sys.exit()
        alle_pos1 = line.index('allele1 - ' + allele.lower())
        alle_pos2 = alle_pos1 + 1
        continue
    if not readfrom: continue
    line = a.strip().split(sep)
    if alle_pos2 > len(line):
        bomb(
            "Probable error in the separator.. Position of Allele2 found in " + alle_pos2 + ", but length of line in row " + en + " is " + len(
                line) + " !!" + \
            "\n       Please check your choice of separator is correct and that you don't have strange fields in you FinalReport file!")

