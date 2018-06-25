# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 21:56:26 2017

@author: mmakwana
"""
def div(D):
    def gen(num):
        return 
    N = 1
    div = 100
    count = 0
    result = 0
    result_str ="."
    while count <= div:
        if D > N :
            if N == 0: break
            N = N * 10
            result *= 10
        else:
            result += N//D
            result_str += str(N//D)
            N = N%D
            count +=1
    print str(result)