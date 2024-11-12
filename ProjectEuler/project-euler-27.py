# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:35:05 2017

@author: mmakwana
"""

def gen_quad_prime(a,b):
    n = 0
    eq = n**2 + a*n + b
    p = is_prime(eq)
    while p:
        yield eq
        n+=1
        eq = n**2 + a*n + b
        p = is_prime(eq)

#P = primes(1000000)
#P = [-i for i in P] + P
def is_prime(n, cache={2:True}):
    n = abs(n)
    print cache
    if n in cache: return cache[n]
    for i in xrange(3,int(n**0.5 + 1)):
        if n%i == 0: 
            cache[n]= False
            return False
    cache[n] = True
    return True

current=(0,0,0)
for a in xrange(-999,1000):
    for b in xrange(-1000,1001):
        prime_len = len([p for p in gen_quad_prime(a,b)])
        if prime_len > current[2]:
            current = (a,b,prime_len)
            print current
print current
print current[0]* current[1]