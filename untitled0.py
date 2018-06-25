# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 18:38:04 2017

@author: mmakwana
"""

from project_euler_tool import factorial

def split_int(n): return map(int, str(n))

def fact_list(n): return [factorial(i) for i in n]

def curious_number(n): return n == sum(fact_list(split_int(n)))

print sum((i for i in xrange(3,1000000) if curious_number(i)))

#total = 0
#for i in range(3,1000000):
#    if curious_number(i): 
#        print i
#        total += i
#
#print total