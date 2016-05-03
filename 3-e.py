# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:01:11 2016

@author: csie3
"""
import thinkdsp
import thinkplot

import pandas as pd

df = pd.read_csv('_taiwanStock.csv', parse_dates=[0])

duration = len(df)
framerate = 1
linewidth = 1

def make_spectrum(signal):
    wave = signal.make_wave(duration=duration, framerate=framerate)
    spectrum = wave.make_spectrum()
    spectrum.hs[0] = 0
    return spectrum
    
signal = thinkdsp.UncorrelatedGaussianNoise()
white = make_spectrum(signal)

signal = thinkdsp.PinkNoise()
pink = make_spectrum(signal)

signal = thinkdsp.BrownianNoise()
red = make_spectrum(signal)

white.plot_power(label='wSpec', color='#000000', linewidth=linewidth)
pink.plot_power(label='pSpec', color='#ff8888', linewidth=linewidth)
red.plot_power(label='rSpec', color='#ff0000', linewidth=linewidth)

thinkplot.config(xlabel='Frequency', ylabel='Power', xscale='log', yscale='log')
