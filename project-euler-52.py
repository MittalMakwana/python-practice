# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:47:45 2017

@author: mmakwana
"""

#def is_permuted(num1,num2): return len(str(num1)) == len(str(num2)) and sorted(str(num1)) == sorted(str(num2))

def is_permuted(lst):
    num = sorted(str(lst[0]))
    lst.pop(0)
    for i in lst:
        if sorted(str(i)) != num:
            return False
    return True
    
    

for x in xrange(1,1000000):
    if is_permuted([i*x for i in xrange(1,7)]):
        print x
        break