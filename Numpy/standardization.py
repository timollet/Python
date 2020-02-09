# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:16:36 2020

@author: goibe
"""

import numpy as np

np.random.seed(0)
A = np.random.randint(0,100,[10,5])
print("Tableau de base :\n",A)
A_mean = A.mean(axis=0)
B = (A - A.mean(axis=0))/ A.std(axis=0)

print("\nTableau standarizé :\n",B)
