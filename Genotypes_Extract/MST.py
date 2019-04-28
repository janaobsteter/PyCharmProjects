import pandas as pd

ped = pd.read_csv("/home/jana/bin/AlphaSim1.05Linux/REAL20GenSel_Class1/GenPed_EBV.txt")
print(ped.head())
print(ped.tail())

ped1 = ped.loc[ped.Generation.isin(range(40, 61))]
print(ped.head())
print(len(ped))

ped.loc[:, "MST"] = None

for row in list(ped1.index):
    parents = [p for p in map(int, list(ped.loc[row, ['Father', 'Mother']]))]
    ped.loc[row, "MST"] = (sum(ped.loc[ped.Indiv.isin(parents), "gvNormUnres1"]) / 2) - ped.loc[row, "gvNormUnres1"]


ped.to_csv("GenPed_MST.csv")

