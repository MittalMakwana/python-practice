# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:40:07 2017

@author: mmakwana
"""

def genmatrix(fname):
    matrix=[]
    with open(fname) as f:
        for i in f:
            i = i[:-1]
            matrix.append(map(int, i.split(",")))
    return matrix

data = genmatrix('')
MATRIX_LEN=80
# Create an empty matrix
l=[[0 for i in range(MATRIX_LEN)] for j in range(MATRIX_LEN)]

l[0][0]=data[0][0]
  
for i in xrange(1,MATRIX_LEN):
    l[i][0]= l[i-1][0]+data[i][0]
for i in xrange(1,MATRIX_LEN):
    l[0][i]=l[0][i-1]+data[0][i]

for i in xrange(1,MATRIX_LEN):
    for j in xrange(1,MATRIX_LEN):
        l[i][j]= data[i][j] + min(l[i-1][j],l[i][j-1])

print l[-1][-1]

