# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 14:28:40 2017

@author: mmakwana
"""
def gen_prime(n):
    A = [True] * (n+1)
    A[0] = False
    A[1] = False
    for i in xrange(int(len(A)**0.5)+1):
        if A[i]:
            for j in xrange(i**2,n+1,i):
                A[j] = False
    return [i for i in xrange(len(A)) if A[i]]

def is_pandigital(num):
    return len(set(map(int , str(num)))) == len(str(num)) and max(set(map(int , str(num)))) == len(str(num)) and 0 not in set(map(int , str(num)))

A = gen_prime(10000000)
max_ = 0
for i in A:
    if is_pandigital(i):
        max_ = i
print max_