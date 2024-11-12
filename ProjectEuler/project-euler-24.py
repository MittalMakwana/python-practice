# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:51:38 2017

@author: mmakwana
"""

def gen_pandigital():
    def is_uniq(n): return len(str(n)) == len(set(str(n)))
    n = '012'
    while n == '210':
        if is_uniq(n):
            yield n
        if n[0] == '0':
            n = '0'+str(int(n)+1)
        else:
            n = str(int(n)+1)
def is_uniq(n): return 

#A = gen_pandigital()
#count = 1
#for i in xrange(1000000):
#    print next(A)
    
 