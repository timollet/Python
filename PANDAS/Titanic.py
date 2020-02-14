# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:23:49 2020

@author: tgoibeau
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#on récupère les données du titanic
data = pd.read_excel('titanic3.xls')

#affiche la forme du tableu
#print(data.shape)

#affiche les premières ligne du tableau
#print (data.head)

#supprime les colonnes 
data = data.drop(['name','sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'],axis=1)

#donne les stats par colonne
print(data.describe())

#supprime les lignes ou il manque une donnée
data = data.dropna(axis=0)
plt.figure()
# va compter les répétitions
data['pclass'].value_counts().plot.bar()
plt.figure()
data['age'].hist()
# groupby comme en sql
print(data.groupby(['sex','pclass']).mean())