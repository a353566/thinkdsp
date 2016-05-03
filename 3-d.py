# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:51:08 2016

@author: csie3
"""
import thinkdsp
import thinkplot

import pandas as pd

df = pd.read_csv('_taiwanStock.csv', parse_dates=[0])

duration = len(df)
framerate = 1
linewidth = 1

signal = thinkdsp.UncorrelatedGaussianNoise()
white = signal.make_wave(duration=duration, framerate=framerate)

signal = thinkdsp.PinkNoise()
pink = signal.make_wave(duration=duration, framerate=framerate)

signal = thinkdsp.BrownianNoise()
red = signal.make_wave(duration=duration, framerate=framerate)

white.plot(label='wNoise', color='#000000', linewidth=linewidth)
pink.plot(label='pNoise', color='#ff8888', linewidth=linewidth)
red.plot(label='rNoise', color='#ff0000', linewidth=linewidth)

thinkplot.config(xlabel='Time', ylim=[-6, 6], xlim=[0, len(df)], legend=True)
