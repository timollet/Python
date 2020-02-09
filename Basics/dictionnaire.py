# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:02:06 2020

@author: goibe
"""

classeur ={
        "positif" : [],
        "negatif" : []        
        }


def trier (classeur , nombre):
    # classeur : dictionnaire de taille 2
    # nombre : int
    # Range un nombre dans "positif" ou "negatif" de classeur selon le signe de nombrte
    
    if (nombre <0):
        
        classeur["negatif"].append(nombre)
    else:
        
        classeur["positif"].append(nombre)
    return classeur

classeur = trier(classeur,1)
print(classeur)
classeur = trier(classeur,-395)
print(classeur)
classeur = trier(classeur,0)
print(classeur)
            