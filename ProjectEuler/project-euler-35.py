# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 22:05:57 2017

@author: mmakwana
"""

def roate(n): return [int(str(n)[-i:] + str(n)[:-i]) for i in xrange(len(str(n)))]

#def roate(n):
#    lst = []
#    for i in str(n):
#        n = int(str(n)[1:] + str(n)[0])
#        lst.append(int(str(n)[1:] + str(n)[0]))
#        lst.sort()
#    return lst

def is_prime(num):
    if num == 2 : return True
    if num %2 == 0:
        return False
    for i in xrange(3,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def gen_prime(num):
    for i in xrange(2,num+1):
        for j in xrange(2,i + 1):
            if i==j:
                yield i
            elif i % j == 0:
                break

def gen_prime2(num):
   A = [True for i in xrange(num)] 
   A[0] = False
   A[1] = False
   
   for i in xrange(int(num**0.5)+1):
       if A[i]:
           for j in xrange(i**2,num,i):
               A[j] = False
   return [i for i in xrange(len(A)) if A[i]]

def is_rotate_prime(num): return all(is_prime(i) for i in roate(num))

count = 0
primes = gen_prime2(1000000)
for i in primes:
    if is_rotate_prime(i):
        count +=1
print count
        
