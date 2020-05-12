# if (!requireNamespace("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# BiocManager::install(version = "3.10")

BiocManager::install("gdsfmt")
BiocManager::install("SNPRelate")

library(SNPRelate)
library(gdsfmt)

library("devtools")
# install_github("zhengxwen/gdsfmt")
# install_github("zhengxwen/SNPRelate")


vcf.fn <- "/home/jana/PycharmProjects/CebeleGeno/MERGED.vcf"
snpgdsVCF2GDS(vcf.fn, "Cebele.gds")
genofile <- snpgdsOpen("Cebele.gds")

snpSet <- snpgdsSelectSNP(genofile, autosome.only=FALSE, remove.monosnp=FALSE)


pca <- snpgdsPCA(genofile, snp.id=snpSet, num.thread=2, autosome.only=FALSE, remove.monosnp=FALSE)
pca
head(pca$eigenval)
head(round(pca$varprop*100, 2))
plot(pca, 1:4)        
