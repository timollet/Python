# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:56:55 2020

@author: tgoibeau
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv('iris.csv')
#sns.pairplot(iris)
#sns.pairplot(iris, hue='variety')

titanic = sns.load_dataset('titanic')
titanic.drop(['alone', 'alive', 'who', 'adult_male', 'embark_town', 'class'], axis=1, inplace=True)
titanic.dropna(axis=0, inplace=True)
print(titanic.head())
#sns.pairplot(titanic)
#sns.catplot(x='pclass',y='age',data=titanic, hue='sex')
#sns.boxplot(x='pclass',y='age',data=titanic, hue='sex')
sns.distplot(titanic['fare'])
sns.jointplot('age','fare', data=titanic, kind='kde')
plt.show()
sns.heatmap(titanic.corr())