# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 15:37:37 2017

@author: mmakwana
"""    

def is_pen(num):
    x = ((24*num+1)**0.5+1)/6
    return x == int(x)

def gen_pen():
    n = 1
    while True:
        yield n*(3*n - 1)/2
        n += 1

pen = lambda n : n*(3*n - 1)/2

for i in xrange(1,2500):
    for j in xrange(i,2500):
        if is_pen(pen(i)+pen(j)) and is_pen(pen(j)-pen(i)):
            print pen(i),pen(j), pen(j) - pen(i)