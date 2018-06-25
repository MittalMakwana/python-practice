# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:26:12 2017

@author: mmakwana
"""

def S(n):
    pass

def P(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

P7=P(1000000)

A = reduce(lambda x,y: x + y, [str(i) for i in P7])