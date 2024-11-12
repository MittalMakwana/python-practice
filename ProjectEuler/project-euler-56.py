# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:32:15 2017

@author: mmakwana
"""

def gen_sum_num(num): return int(reduce(lambda x,y: int(x)+int(y), str(num)))

max_ = 0
for i in xrange(1,100):
    for j in xrange(1,100):
        if gen_sum_num(i**j) > max_: 
            print i, j
            max_ = gen_sum_num(i**j)
print max_