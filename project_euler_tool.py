# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 14:28:40 2017

@author: mmakwana
"""
def sum_of_n(n): return (n*(n+1)/2)
def sum_of_square(n): 
    '''
    Find sum of 1^2 + 2^2 + 3^2 + 4^2...n^n
    Can also be use to find number of square inside a square grid of n X n
    '''
    return (n*(n+1)*(2*n + 1)/6)
def sum_of_cube(n): return (sum_of_n(n)**2)

def total_square(a,b):
    '''
    returns a*(a+1)*(2*a+1)/6 + (b-a)*a*(a+1)/2
    a*(a+1)*(2*a+1)/6 = find number of square inside a square grid of a X a
    (b-a)*a*(a+1)/2 = total number of squares increased is (n-m)*m(m+1)/2.
    http://www.geeksforgeeks.org/count-number-of-squares-in-a-rectangle/
    '''
    if b < a: a,b = b,a
    return a*(a+1)*(2*a+1)/6 + (b-a)*a*(a+1)/2


def total_rectangle(a,b):
    '''
    Retuerns total number of rectangle in
    a x b grid
    '''
    return (a*(a+1)*b*(b+1)/4)
    
def sum_of_square_alter(n, a, d):
#    Σn^2(a,d) =  ;
    return (n*(a**2))+((1/6)*(d**2)*n*(n-1)*(2*n-1))+(a*n*d*(n-1))



def sum_of_range(start,end): return (sum_of_n(end) - sum_of_n(start - 1))
def sum_of_range_square(start, end): return (sum_of_square(end) - sum_of_square(start - 1))

def is_palindrom(s): return str(s) == str(s)[::-1]



def nCr(n,r):
    '''
    returns the value of 
    nCr =	n!
        r!(n−r)!
    where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
    
    Usage:
        There are exactly ten ways of selecting three from five, 12345:
            
            123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

        In combinatorics, we use the notation, 5C3 = 10.
    '''
    if 0 < r <=n :
        return factorial(n)/(factorial(r) * factorial(n - r))
    else:
        print "n and r value are incorrect"

def binomenial_co_effecient(a,b): 
    '''
    Can be used to generate pascal traiangle
    or for coeffeient for (x+y)^n
    (a)
    (b)
    is eqaula to a!/b!(a-b)!
    a>=b>=0
    '''
    return (factorial(a)/(factorial(b)*factorial(a-b)))

def fibonaci(to):
    a = 1
    b = 1
    while a < to:
        yield a
        a,b = b , a + b

#print [x for x in xrange(2,1000000) if not [t for t in xrange(2,int(x**0.5)+1) if not x%t]]

def gen_prime(n):
    A = [True] * (n+1)
    A[0] = False
    A[1] = False
    for i in xrange(int(len(A)**0.5)+1):
        if A[i]:
            for j in xrange(i**2,n+1,i):
                A[j] = False
    return [i for i in xrange(len(A)) if A[i]]

def factor(num):
    n = 2
    result = []
    while num > 1:
        if num % n == 0 :
            result.append(n)
            num = num / n
        else:
            n +=1
    return result