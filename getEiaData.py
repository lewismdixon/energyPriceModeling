#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 22:05:50 2021

@author: lewisdixon
"""

import json
import requests
import numpy as np
import pandas as pd

#series ID = AEO.2021.REF2021.PRCE_NA_ELEP_GEN_ELC_NA_PJMW_NCNTPKWH.A
#API Key = 0a9c80059ad9bd5dab86eb9fd6df1441
url = "http://api.eia.gov/series/?api_key=0a9c80059ad9bd5dab86eb9fd6df1441&series_id=AEO.2021.HIGHMACRO.PRCE_NA_ELEP_GEN_ELC_NA_PJMW_Y13CNTPKWH.A"
response = requests.get(url)

eVals = json.loads(response.text)

seriesList = eVals['series']

dataContentsDict = seriesList[0]

dataContentsList = dataContentsDict['data']
#dataContentsTable = pd.DataFrame(dataContentsDict['data'][][0],dataContentsDict['data'][][1],['Year','$/KWh'])
yearsObs = []
for obsIndex in range(len(dataContentsList)): 
    yearsObs = yearsObs + [dataContentsList[obsIndex][0]]

print(yearsObs)
print("you so cool")



