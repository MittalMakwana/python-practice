# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:46:45 2017

@author: mmakwana
"""


def gen_square_chain(num):
    def make_num(num): return (reduce(lambda x,y: x+y, map(lambda x: int(x)**2, str(num))))
    if num == 1:return 1
    elif num == 89: return 89
    else: return gen_square_chain(make_num(num))

count = 0
for i in xrange(2,10000000):
    if gen_square_chain(i) == 89: count +=1
print count