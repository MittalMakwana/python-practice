# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 14:40:39 2017

@author: mmakwana
"""



def gen_prime(num=9999):
    '''
    
    Generate prime number using  sieve of Eratosthenes
    which is the quickest way to find prime till 1 to 1000000
    
    '''
    A = [True]*(num)
    A[0] = False
    A[1] = False
    for i in xrange(int(len(A)**0.5)+1):
        if A[i]:
            for j in xrange(i**2,num,i):
                A[j] = False
                
    return [i for i in xrange(len(A)) if A[i] and i > 1480]


def are(a,b,c): 
    return len(str(a)) == len(str(b)) == len(str(c)) and sorted(str(a)) == sorted(str(b)) == sorted(str(c)) and a != b !=c

A = gen_prime()
DIFF = 3330
#for i in xrange(int(len(A))/2):
#    for j in xrange(i, len(A)):
#        for k in xrange(len(A) - 1, j, -1):
#            if are(A[i], A[j], A[k]) and A[j] - A[i] == A[k] - A[j]:
#                print A[i], A[j], A[k], A[j] - A[i], A[k] - A[j]
#                break


for i in A:
    if i in A and i + DIFF in A and i + DIFF + DIFF in A and are(i,i + DIFF,i + DIFF + DIFF):
        print i , i + DIFF,i + DIFF + DIFF , DIFF
