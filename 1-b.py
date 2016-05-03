# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:37:29 2016

@author: csie3
"""
import thinkdsp
import thinkplot

### Square
signal = thinkdsp.SquareSignal(100)
wave = signal.make_wave(duration=0.5, framerate=10000)
SquareSpec = wave.make_spectrum().plot(color='#0000ff')

### sine 可能被蓋掉所以放到第二個
signal = thinkdsp.SinSignal(freq=100, amp=1)
wave = signal.make_wave(duration=0.5, framerate=10000)
sine = wave.make_spectrum().plot(color='#abcdef')

### Sawtooth
signal = thinkdsp.SawtoothSignal(100)
wave = signal.make_wave(duration=0.5, framerate=10000)
SawtoothSpec = wave.make_spectrum().plot(color='#00ff00')

### Triangle
signal = thinkdsp.TriangleSignal(100)
wave = signal.make_wave(duration=0.5, framerate=10000)
TriangleSpec = wave.make_spectrum().plot(color='#ff0000')

thinkplot.config(xlabel='Frequency', ylabel='Power')





