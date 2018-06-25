# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:51:12 2017

@author: mmakwana
"""

def total_rectangle(a,b):
    '''
    Retuerns total number of rectangle in
    a x b grid
    '''
    return (a*(a+1)*b*(b+1)/4)

rec = (0,0,0,0)
for a in xrange(1,100):
    for b in xrange(1,a):
        if total_rectangle(a,b) < 2000000 and rec[2] < total_rectangle(a,b):
            rec = a,b,total_rectangle(a,b),a*b
            print rec