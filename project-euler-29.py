# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 18:12:28 2017

@author: mmakwana
"""

#def powers(base, end): return [base**i for i in xrange(2,end+1)]

if __name__ == '__main__':
    number = set()
    for a in xrange(2,101):
        for b in xrange(2,101):
            number.add(a**b)
    print len(number)