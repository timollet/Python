# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:13:23 2020

@author: goibe
"""
import numpy as np

"""
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (A)
#slicing
print("\n",A[:,1])
B = A[0:2,0:2]

print("\n",B)

print("\n",A[:,-2:])

B = np.zeros((4,4))
print("\n",B)

B[1:3,1:3] = 1
print("\n",B)

C = np.zeros((5,5))
print("\n",C)
C[::2,::2]=1
print("\n",C)

#Boolean indexing/masking
A = np.random.randint(0,10,[5,5])
print("\n",A)
print("\n",A<5)

A[A<5] = 10
print("\n",A)
A[(A<5) & (A>2)] = 10
print("\n",A)
print("\n",A[A<10])
B = np.random.randn(5,5)
print("\n",B)
C = B
C[A>6] = C[A>6] + -10
print("\n",C)
"""

#Exercice
from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray=True)
basic_shape = face.shape

h = basic_shape[0]//4
w = int(basic_shape[1]/4)

zoom_face = face[h:-h,w:-w]
zoom_face[zoom_face>120]=255
zoom_face[zoom_face<121]=0

plt.imshow(zoom_face,cmap=plt.cm.gray)
plt.show()

#fausse compression
face[::2,::2]
plt.imshow(face,cmap=plt.cm.gray)
plt.show()


