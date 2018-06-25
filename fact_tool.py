# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:36:14 2017

@author: mmakwana
"""
import math

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def fact_trailling_zero(n): 
    '''
    parm: n natural number to get trailing zero in a factorail of large number
    Formula explained in https://brilliant.org/wiki/trailing-number-of-zeros/
    '''
    if n < 1: 
       raise ValueError('Negative number less than 1 not aceppted')
    return sum((n/5**i for i in range(1,int(math.log(n,5))+1)))

def fact_number_digits(n):
    