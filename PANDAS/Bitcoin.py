# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:52:38 2020

@author: tgoibeau
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bitcoin = pd.read_csv('BTC-EUR.csv', index_col='Date', parse_dates=True)
plt.figure()
bitcoin['Close'].plot(figsize=(9,6))
plt.show()
print(bitcoin.index)

plt.figure(figsize=(12,8))
bitcoin['2019']['Close'].plot()
bitcoin['2019']['Close'].resample('M').mean().plot(label='moyenne par mois', lw=3, ls=':', alpha=0.8)
bitcoin['2019']['Close'].resample('W').mean().plot(label='moyenne par semaine', lw=2, ls='--', alpha=0.8)
plt.legend()
plt.show()

m = bitcoin['2019']['Close'].resample('W').agg(['mean', 'std', 'min', 'max'])
plt.figure(figsize=(12,8))
m['mean']['2019'].plot(label='moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha=0.2, label='min-max par semaine')
plt.legend()
plt.show()


plt.figure(figsize=(12,8))
bitcoin['2019-09']['Close'].plot()
bitcoin['2019-09']['Close'].rolling(window=7).mean().plot(label='moving average', lw=3, ls=':', alpha=0.8)
bitcoin['2019-09']['Close'].rolling(window=7, center=True).mean().plot(label='moving average', lw=3, ls=':', alpha=0.8)
bitcoin['2019-09']['Close'].ewm(alpha=0.5).mean().plot(label='moving average', lw=3, ls=':', alpha=0.8)
plt.show()


ethereum = pd.read_csv('ETH-EUR.csv', index_col='Date', parse_dates=True)
plt.figure(figsize=(12,8))
ethereum['2019']['Close'].plot()
plt.show()

btc_eth = pd.merge(bitcoin, ethereum, on='Date', how='inner', suffixes=('_btc','_eth'))
btc_eth[['Close_btc', 'Close_eth']].plot(subplots=True,figsize=(12,8))
plt.show()
print(btc_eth[['Close_btc', 'Close_eth']].corr())


#Exercice stratégie de la tortue
bitcoin['Sell']=np.zeros(len(bitcoin))
bitcoin['Buy']=np.zeros(len(bitcoin))
bitcoin.loc[ bitcoin['Close'] >= bitcoin['Close'].rolling(window=28).max() , 'Buy'] = 1
bitcoin.loc[ bitcoin['Close'] <= bitcoin['Close'].rolling(window=28).min() , 'Sell'] = -1 
plt.figure(figsize=(12,8))
bitcoin['2019']['Close'].plot()
bitcoin['2019']['Close'].rolling(window=28).max().plot()
bitcoin['2019']['Close'].rolling(window=28).min().plot()
plt.show()
plt.figure(figsize=(12,8))
bitcoin['2019']['Buy'].plot()
bitcoin['2019']['Sell'].plot()
plt.show()