# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:07:56 2017

@author: mmakwana
"""

def gcd(a, b):
    while a != b:
        if a > b:
           a = a - b
        else:
           b = b - a
    return a