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
plt.scatter(x, y)
plt.plot(new_x, result, c='r')