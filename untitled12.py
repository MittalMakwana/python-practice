# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:46:23 2017

@author: mmakwana
"""

def gen_rt_tri(p):
    tri =[]
    for a in xrange(1,p/2):
        for b in xrange(1, p/2):
                if a**2 + b**2 == (p - (a+b))**2 and a < b:
                    tri.append({a, b , p - a - b})
    return tri

p = 1
max_sol = 0
max_list = []
while p <= 1000:
    if len(max_list) < len(gen_rt_tri(p)):
        max_list = gen_rt_tri(p)
        max_sol = p
        print max_list, p
    p += 1