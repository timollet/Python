# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:16:13 2020

@author: goibe
"""
import numpy as np
x = np.linspace(0,2,10)
y = x**2
#1 pypplot
import matplotlib.pyplot as plt
''' Test

plt.plot(x,y, c="red" , lw=5, ls="--")
plt.show()
plt.scatter(x,y)
plt.show()

plt.figure(figsize=(12,8))
plt.plot(x,y, label="quadratique")
plt.plot(x,x**3, label="cubique")
plt.title("figure 1")
plt.xlabel("axe x")
plt.ylabel("axe y")
plt.legend()
plt.show()
plt.savefig("figure.png")

plt.figure()
plt.subplot(2,1,1)
plt.plot(x,y,c="red")
plt.subplot(2,1,2)
plt.plot(x,y,c="blue")
plt.savefig("figure2.png")
'''
#Excercice 1
dataset = {f"experience{i}": np.random.randn(100,3) for i in range(4)}
#for i in range (4):
#   print("\n",dataset[f"experience{i}"])

def graphique(dataset):
    n =len(dataset)
    plt.figure(figsize=(12,8))
    for k,i in zip(dataset.keys(), range(1,n+1)):
            plt.subplot(n,1,i)
            plt.plot(dataset[k])
            plt.title(k)
    
    plt.savefig("graphique.png")
            
graphique(dataset=dataset)


#Excercice 2
 
# Matrice de corrélation des iris
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

def graphique_iris(x):
    n = x.shape[1]
    plt.figure(figsize=(12,8))
    for i in range(n):
            plt.subplot(n//2,n//2,i+1)
            plt.scatter(x[:,0],x[:,i], c=y)
            plt.xlabel("0")
            plt.ylabel(i)
    
    plt.savefig("graphique.png")
            
graphique_iris(x=X)