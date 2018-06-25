# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:43:22 2017

@author: mmakwana
"""

from project_euler_tool import nCr

count = 0
for n in xrange(1,101):
    for r in xrange(1,n):
        if nCr(n,r) >= 1000000:count +=1
print count