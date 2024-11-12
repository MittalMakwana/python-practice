# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:47:13 2017

@author: mmakwana
"""
def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def nPr(n,r):
    if 0 < r <=n :
        return factorial(n)/factorial(n - r)
    else:
        print "n and r value are incorrect"