# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 09:50:29 2017

@author: mmakwana
"""

def gen_prime2(num):
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
    return [i for i in xrange(len(A)) if A[i]]


def is_prime(num):
    '''
    Function to check if a given number is prime or not
    
    '''
    for i in xrange(2,int(num**0.5)+1):
        if num % i == 0: return False
    return True


LIMIT = 1000000
primes = gen_prime2(LIMIT)

# 
window = 0

# Counter to sotre the maximum prime number found out
max_total = 0

# Counter to store the current max cosecutive prime sum found out
max_conc = 0

# This is is to incress the window size
# The upper limit is set to square root of the lent of primes
while window < len(primes)**0.5:
    
#    Loop to fin out sum of cosecutive primes
    for i in xrange(window,len(primes)):
        if max_total <= sum(primes[window:i]) and \
        is_prime(sum(primes[window:i])) and \
        max_conc < len(primes[window:i]):
            
            # Break the for loop is the sum of prime is crossing the desired limit
            if sum(primes[window:i]) > LIMIT:
                break
#           print primes[window:i]
#           Debug line
#           prints first and last prime number sum and lenght
            print "[",
            print primes[window], 
            print "-",
            print primes[i], 
            print "]",
            print sum(primes[window:i]), len(primes[window:i])
            # This is the actual result
            max_total = sum(primes[window:i])
            max_conc = len(primes[window:i])
    window += 1