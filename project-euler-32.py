# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:57:57 2017

@author: mmakwana
"""

def is_pandigital(a, b, num):
    if a * b == num:
        map_a = map(int, str(a))
        map_b = map(int, str(b))
        map_num = map(int, str(num))
        result = map_a + map_b + map_num
        result.sort()
        return result == range(1,10)
    return False   
t = 0 

def is_uniq(n): return len(str(n)) == len(set(str(n)))
t = set()
for i in xrange(1,100):
    if is_uniq(i):
        for j in xrange(i,9999):
            if is_uniq(j):
                if is_pandigital(i,j,i*j) and len(str(i)) + len(str(j)) + len(str(i*j)) == 9:
                    print i , j , i*j
                    t.add(i*j)

print t
        
