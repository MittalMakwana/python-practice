# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:33:17 2017

@author: mmakwana
"""

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))
