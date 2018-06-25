# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 19:20:05 2017

@author: mmakwana
"""
def gen_tri():
    n = 0
    while True:
        n += 1
        yield n*(n+1)/2

def gen_pen():
    n = 0
    while True:
        n += 1
        yield n*(3*n-1)/2

def gen_hex():
    n = 0
    while True:
        n += 1
        yield n*(2*n-1)

T = gen_tri()
P = gen_pen()
H = gen_hex()

last_T = next(T)
last_P = next(P)
last_H = next(H)

while True:

    if last_T < last_H:
        last_T = next(T)    
    elif last_P < last_H:
        last_P = next(P)
    else:
        last_H = next(H)
    if last_T == last_P == last_H and last_T > 40755:
        print last_T
        break
#    print last_T,last_P, last_H