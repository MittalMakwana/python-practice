# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:15:53 2017

@author: mmakwana
"""            
#data = (
#        
#[3],
#[7, 4],
#[2, 4, 6],
#[8, 5, 9, 3],
#        )

data=()
with open('p18.txt') as f:
    for i in f:
        data = data + (map(int, i.strip("\n").split(" ")),)

for i in xrange(len(data)-1,0,-1):
    for j in xrange(len(data[i-1])):
        data[i-1][j] += max(data[i][j],data[i][j+1])
#        if data[i][j] > data[i][j+1]:
#            data[i-1][j] = data[i-1][j]+data[i][j]
#        else:
#            data[i-1][j] = data[i-1][j]+data[i][j+1]

for i in data:
    print i
print data[0]