import numpy as np
import copy
import pickle
import os
import matplotlib.pyplot as plt
import sys
sys.path.append(os.getcwd())
# current dir
cdir = os.getcwd()
print(cdir)

# specific seqbreed modules
# USE THIS if importing from src files directly
from SeqBreed import genome as gg
from SeqBreed import selection as sel

wdir = os.getcwd()
vcffile = wdir + "/MERGED.vcf"
seqfile = 'seq.pos'

gbase = gg.GFounder(vcfFile = vcffile, snpFile = seqfile)

gfeatures = gg.Genome(snpFile=seqfile, ploidy=gbase.ploidy,  XChr='X', YChr='Y', MTChr='MT')
