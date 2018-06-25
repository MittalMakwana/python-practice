# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 23:42:17 2017

@author: mmakwana
"""

def d_to_b(num): return bin(num)[2:]

def is_pali(num): return str(num) == str(num)[::-1]

print sum(( i for i in xrange(1,1000000) if is_pali(i) and is_pali(d_to_b(i))))