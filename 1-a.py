# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:20:28 2016

@author: csie3
"""

import thinkdsp
import thinkplot

### Sine
signal = thinkdsp.SinSignal(100)
Sine = signal.make_wave(duration=0.03, start=0, framerate=10000).plot()

### Square
signal = thinkdsp.SquareSignal(100)
Square = signal.make_wave(signal.period*3, framerate=10000).plot(color = '#0000ff')

### Triangle
signal = thinkdsp.TriangleSignal(100)
Triangle = signal.make_wave(signal.period*3, framerate=10000).plot(color = '#ff0000')

### Sawtooth
signal = thinkdsp.SawtoothSignal(100)
Sawtooth = signal.make_wave(signal.period*3, framerate=10000).plot(color = '#00ff00')

thinkplot.config(ylim=[-1.05, 1.05])
