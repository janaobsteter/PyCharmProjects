# -*- coding: utf-8 -*-
from __future__ import division
import sys
import os
import math
from selection10 import *
from selection10 import nastavi_cat, selekcija_total
from collections import defaultdict
import shutil
import pandas as pd
import numpy as np
import resource
import ast

WorkingDir = '/home/v1jobste/JanaO/'




######################################################################################
######################################################################################
# os.chdir("/home/jana/bin/AlphaSim1.05Linux/EddieScripts/")
# argument 0 is the name of the script
refSize = "10K"

name = "True10_1_1"



par = pd.read_csv(WorkingDir + "/SelPar/" + refSize + "_Pheno/SelectionParam_Gen_MaleGS_" + name + ".csv", header=None, names=["Keys", "Vals"])
par.to_dict()
selPar = defaultdict()

for key, val in zip(par.Keys, par.Vals):
    if key not in ['BurnInYN', 'EBV', 'gEBV', 'PA', 'AlphaSimDir', 'genotyped', 'genotypedAge', 'EliteDamsPTBulls',
                   'EliteDamsPABulls', 'UpdateGenRef', 'sexToUpdate', 'EliteDamsGenBulls', 'gpb_pb',
                   'genTest_mladi', 'genTest_gpb', 'genFemale', 'maleGenSelAll']:
        try:
            selPar[key] = int(val)
        except:
            selPar[key] = float(val)
    if key in ['BurnInYN', 'EBV', 'gEBV', 'PA', 'AlphaSimDir', 'EliteDamsPTBulls',
               'EliteDamsPABulls', 'UpdateGenRef', 'EliteDamsGenBulls', 'gpb_pb',
               'genTest_mladi', 'genTest_gpb', 'genFemale', 'maleGenSelAll']:
        if val in ['False', 'True']:
            selPar[key] = bool(val == 'True')
        else:
            selPar[key] = val
    if key in  ['genotyped', 'genotypedAge']:
        selPar[key] = ast.literal_eval(val)
    if key == 'sexToUpdate':
        selPar[key] = ast.literal_eval(val) if len(ast.literal_eval(val)) > 1 else ast.literal_eval(val)[0]

BurnInYN = "False"  # ali izvedeš tudi BurnIn
SelYN = "True"  # ali izvedeš tudi BurnIn
StNB = 8640
StBurnInGen = 20
StFillInBurnIn = 40
StSelGen = 40
StartSelGen = 21
StopSelGen = 40
NumberOfSires = 12
NumberOfDams = 4320
selPar['AlphaSimDir'] = os.getcwd() + '/'
AlphaSimDir = os.getcwd() + '/'
AlphaSimPed = selPar['AlphaSimDir'] + '/SimulatedData/PedigreeAndGeneticValues.txt'
if selPar['EBV']:
    seltype = 'class'
if selPar['gEBV']:
    seltype = 'gen'


selekcija_total('GenPed_EBV.txt', **selPar)


