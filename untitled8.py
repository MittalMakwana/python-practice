# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 12:30:50 2017

@author: mmakwana
"""

def trunc_right(num): return [int(str(num)[:i]) for i in xrange(1,len(str(num))+1)]
def trunc_left(num):return [int(str(num)[i:]) for i in xrange(len(str(num)))]
def trunc(num): return set(trunc_right(num) + trunc_left(num))
    
def is_prime(num):
    if num < 2 : return False
    for i in xrange(2,int(num**0.5)+1):
        if num % i == 0: return False
    return True

def is_primelist(lst):
    for i in lst:
        if not is_prime(i): return False
    return True

def lst_prime(num):
    A = [True] * (num)
    A[0] = False
    A[1] = False
    for i in xrange(int(num**0.5)+1):
        if A[i]:
            for j in xrange(i**2,num,i):
                A[j] = False
    return [i for i in xrange(len(A)) if A[i]]

def gen_prime(num):
    for i in xrange(2,num+1):
        for j in xrange(2,i + 1):
            if i==j:
                yield i
            elif i % j == 0:
                break

count = 0
sum_ = 0
for i in lst_prime(1000000):
    if is_primelist(trunc(i)) and i > 7 and count < 12:
        print i
        sum_ += i
        count +=1
    