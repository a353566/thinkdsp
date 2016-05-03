# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:23:42 2016

@author: csie3
"""
import pandas as pd

pData = pd.read_csv('_taiwanStock.csv',parse_dates=[0])
print(len(pData))
