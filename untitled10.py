# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 00:58:47 2017

@author: mmakwana
"""

def lst_prime(num):
    A = [True] * (num)
    A[0] = False
    A[1] = False
    for i in xrange(int(num**0.5)+1):
        if A[i]:
            for j in xrange(i**2,num,i):
                A[j] = False
    return [i for i in xrange(len(A)) if A[i]]

def sq(n):return n <=10
def sum_of_n(n): return (n*(n+1)/2)
b = lambda a,b : a+b
a = lambda n: n*(n+1)/2
print map(sq ,  [1,2,30,4])
print map(b, 1,2)
print map(a, [1,2,3,4,5,6,7])