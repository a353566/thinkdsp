# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:29:28 2016

@author: csie3
"""
import pandas as pd

pData = pd.read_csv('_taiwanStock.csv',parse_dates=[0])
print(pData[len(pData)-10:len(pData)])
