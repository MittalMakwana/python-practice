# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:09:58 2017

@author: mmakwana
"""

def is_pandigital(num):
    n = map(int, str(num))
    n.sort()
    return n == [1,2,3,4,5,6,7,8,9]

for i in xrange(1,10000):
    l = 9
    string = ''
    for j in xrange(1,10):
        l = l - len(str(i*j))
        if l < 0: break
        string += str(i*j)
        if is_pandigital(string):
            print str(i) + " 1.."+ str(j) + " = "+ string