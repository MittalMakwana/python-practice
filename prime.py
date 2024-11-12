# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:31:10 2017

@author: mmakwana
"""
import datetime
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def gen_prime(n):
    A = [True] * (n+1)
    A[0] = False
    A[1] = False
    for i in xrange(int(len(A)**0.5)+1):
        if A[i]:
            for j in xrange(i**2,n+1,i):
                A[j] = False
    return [i for i in xrange(len(A)) if A[i]]

