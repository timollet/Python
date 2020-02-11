# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:32:26 2020

@author: goibe
"""


import numpy as np
import matplotlib.pyplot as plt

''' 1 Interpolation '''
# Création d'un Dataset
x = np.linspace(0, 10, 10)
y = np.sin(x)
plt.scatter(x, y)

from scipy.interpolate import interp1d

# création de la fonction interpolation f
f = interp1d(x, y, kind='cubic')

# résultats de la fonction interpolation f sur de nouvelles données
new_x = np.linspace(0, 10, 50)
result = f(new_x)

# visualisation avec matplotlib
plt.figure()
plt.scatter(x, y)
plt.plot(new_x, result, c='r')

''' 2 Optimize '''
x = np.linspace(0, 2, 100)
y = 1/3*x**3 - 3/5 * x**2 + 2 + np.random.randn(x.shape[0])/20

def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x +d

from scipy import optimize

params, param_cov = optimize.curve_fit(f, x, y)
plt.figure()
plt.scatter(x,y)
plt.plot(x, f(x, params[0], params[1], params[2], params[3]), c="g", lw=3)

def g (x):
    return x**2 + 15*np.sin(x)
x = np.linspace(-10, 10, 100)
x0=-5

result = optimize.minimize(g, x0=x0).x
plt.figure()
plt.plot(x, g(x), lw=3,zorder=-1)
plt.scatter(result, g(result), s=100, c="r",zorder=1)
plt.scatter(x0, g(x0), s=200, marker="+", c="g",zorder=1)
plt.show()

''' 3 Traitement de signal '''
x = np.linspace(0,20, 100)
y = x + 4*np.sin(x) + np.random.randn(x.shape[0])
plt.plot(x, y)
from scipy import signal
y_detrend = signal.detrend(y)
plt.plot(x, y_detrend)
#FOURIER
x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x) + np.random.random(x.shape[0])*10
plt.figure()
plt.plot(x,y)
from scipy import fftpack
fourier  = fftpack.fft(y)
power = np.abs(fourier)
frequences = fftpack.fftfreq(y.size)
plt.figure()
plt.plot(np.abs(frequences), power)
fourier[power<400] = 0
power = np.abs(fourier)
plt.figure()
plt.plot(np.abs(frequences), power)
filtered_signal = fftpack.ifft(fourier)
plt.figure(figsize=(12,8))
plt.plot(x,y,lw=0.5)
plt.plot(x,filtered_signal,lw=3)
