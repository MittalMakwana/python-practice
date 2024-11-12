# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 09:30:47 2017

@author: mmakwana

"""
# This is brute force
#s = '.'
#for i in xrange(1,1000000):
#    s += str(i)
#    
#print s[1],s[10],s[100],s[1000],s[10000],s[100000],s[1000000]

def gen_series(start,end): return [i for i in xrange(start,end+1)]


S1 = gen_series(1,9)
S2 = gen_series(10,99)
S3 = gen_series(100,999)