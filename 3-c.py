# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:31:48 2016

@author: csie3
"""
import numpy as np
import pylab as pl

f= open('_taiwanStock.csv')
s= f.read()
sL= s.split('\n')
xL= [x.split(',')[-1] for x in sL]
yL= [float(x) for x in xL[1:-4]]
pData= np.array(yL)

def movingAverage(x, length):
    y= np.convolve(x, np.ones(length)/length)
    y= y[:len(x)]
    return y

ma100=  movingAverage(pData, 100)
ma1000=  movingAverage(pData, 1000)
ma10000= movingAverage(pData, 10000)

pl.plot(pData)
pl.plot(ma100)
pl.plot(ma1000)
pl.plot(ma10000)
