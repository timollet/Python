# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:17:50 2020

@author: goibe
"""

import numpy as np
'''
A = np.array([1,2,3])
print(A.ndim)
print(A.shape)
print(A.size)

B = np.zeros((3,2))
print(B)
print(B.ndim)
print(B.shape)
print(B.size)

C = np.ones((3,2))
print(C)
print(C.ndim)
print(C.shape)
print(C.size)

D = np.full((2,4),8)
print(D)
print(D.ndim)
print(D.shape)
print(D.size)

np.random.seed(0) #pour fixer le meme random a chaque exec
E = np.random.randn(3,4)
print(E)
print(E.ndim)
print(E.shape)
print(E.size)

F= np.eye(4) #matrice identité
print(F)

G = np.linspace(0,10,20)
print(G)

H = np.arange(0,10,0.5)
print(H)

I = np.linspace(0,10,20,dtype=np.float16)
print(I)

hBC = np.hstack((B,C))
print(hBC)
print(hBC.shape)

hBC2 = np.concatenate((B,C),axis=1)#methode a retenir
print(hBC2)
print(hBC2.shape)

vBC = np.vstack((B,C))
print(vBC)
print(vBC.shape)

vBC2 = np.concatenate((B,C),axis=0)#methode a retenir
print(vBC2)
print(vBC2.shape)

vBCreshape = vBC.reshape((3,4))
print(vBCreshape)
vBCravel = vBCreshape.ravel().shape
print(vBCravel)

print(A.shape)
A = A.reshape((A.shape[0],1))
print(A.shape)
A = A.squeeze()
print(A.shape)

'''

# Exercice
def initialisation(m,n):
    # m : nombre de lignes
    # n : nombre de colonnes
    # retourne une matrice aléatoire (m , n+1)
    # avec une colonne biais (remplie de "1") tout a droite
    matrice = np.random.randn(m,n)
    print(matrice)
    matrice = np.concatenate((matrice,np.ones((m,1))),axis=1)
    print(matrice)
    return matrice

initialisation(8,5)