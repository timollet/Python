# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 22:35:12 2020

@author: goibe
"""
'''5 Nuage de point '''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
 
# chargement d'un dataset de fleur d'iris
iris = load_iris()
X = iris.data # X contient 150 échantillons, 4 variables
y = iris.target # y contient 150 échantillons, 3 classes
 
# création d'une boucle for pour afficher tous les graphiques
n = X.shape[1]
plt.figure(figsize=(12, 8))
for i in range(n):
    plt.subplot(n//2, n//2, i+1)
    plt.scatter(X[:, 0], X[:, i], c=y) # affiche la variable i en fonction de la variable 0
    plt.xlabel('0')
    plt.ylabel(i)
    plt.colorbar(ticks=list(np.unique(y)))
plt.show()

''' 4 graphe 3D'''
#%matplotlib # cette ligne permet d'ouvrir une fenêtre QT5 pour zoomer et bouger votre graphique !
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # module 3D de Matplotlib
plt.figure(figsize=(12, 8))
ax = plt.axes(projection='3d') # Création d'un objet "axe 3D"
ax.scatter(X[:, 0], X[:, 1], X[:,2], c=y)

# Création d'une fonction
f = lambda x, y: np.sin(x) + np.cos(y) * np.cos(x)
 
# Création d'un domaine d'étude X, Y
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)
 
# Résultat : tableau numpy 2D
Z = f(X, Y)
 
# Affichage de la surface
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')

''' 3 Histogramme '''
# Générations de données : 1000 points aléatoires normaux
x = np.random.randn(1000)
plt.figure(figsize=(12, 8))
# visualisation sur 50 intervalles
plt.hist(x, bins=50)

#histogramme 2d
plt.figure(figsize=(12, 8))
# visualisation 
X1 = iris.data # X contient 150 échantillons, 4 variables
Y1 = iris.target # y contient 150 échantillons, 3 classes
plt.hist2d(X1[:,0],X1[:,1])
plt.xlabel('longueur sepal')
plt.ylabel('largeur sepal')
plt.colorbar()

''' 2 contour '''
plt.figure(figsize=(12, 8))
X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)
 
Z = f(X, Y)
#plt.contour(X, Y, Z, levels=40)

plt.contourf(X, Y, Z,20,cmap="RdGy")
plt.colorbar()

''' 1 imshow '''
plt.figure(figsize=(12, 3))
 
# Simple graphique imshow()
X = np.random.randn(50, 50)
 
plt.subplot(131)
plt.imshow(X)
 
# Matrice de corrélation des iris
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
 
plt.subplot(132)
plt.imshow(np.corrcoef(X.T, y))
 
# Matrice f(X, Y) = sin(X) + cos(Y)
X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)
 
plt.subplot(133)
plt.imshow(f(X, Y))
plt.colorbar()