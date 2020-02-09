# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:11:46 2020

@author: goibe
"""

import glob
dico2 = {}
filenames = glob.glob("*.txt") # liste tous les fichiers avec l'extension .txt
 
print (filenames)

for file in filenames: # selectionne l'un apres l'autres les fichiers dans filenames
    dico2[file] = [line.strip() for line in open(file,'r')]
    
print(dico2)