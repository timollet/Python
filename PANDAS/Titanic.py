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
# Stats moyennes selon la classe et le sexe
print('--------------------------------------')
print ('\n Stats selon la classe et le sexe \n')
print(data.groupby(['sex','pclass']).mean())
print('\n')
# le nombre de mineur par classe
print('--------------------------------------')
print ('\n Nombre de mineur selon la classe \n')
print(data[data['age'] < 18]['pclass'].value_counts())

# Stats des moyennes sur les mineur selon leur sex et classe
print('--------------------------------------')
print ('\n Stats des mineurs selon la classe et le sexe \n')
print(data[data['age'] < 18].groupby(['sex','pclass']).mean())

# Indexing comme numpy avec iloc (index localisation)
print('--------------------------------------')
print(data.iloc[0:2,0:2])
print('--------------------------------------')
print(data.loc[0:2,['age','sex']])

#Excercice Feature Engineering (categorie d'age)
print('--------------------------------------')
data[ data.loc[:,'age']<21 ] = 0
data[ (data.loc[:,'age']>20) & (data.loc[:,'age']<31)] = 1
data[ (data.loc[:,'age']>30) & (data.loc[:,'age']<41)] = 2
data[ data.loc[:,'age']>40 ] = 3
print(data['age'].value_counts())
