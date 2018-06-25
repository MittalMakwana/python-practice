# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 14:32:35 2017

@author: mmakwana
"""
def dig(n):
    side = [i for i in xrange(3,n+1,2)]
    a = [i**2 for i in xrange(3,n+1,2)]
    b = [x - 1*(y - 1) for x, y in zip(a,side)]
    c = [x - 2*(y - 1) for x, y in zip(a,side)]
    d = [x - 3*(y - 1) for x, y in zip(a,side)]
    
    result = 1 + sum(a)+sum(b)+sum(c)+sum(d)
    return result

def gen_diag(n):
    number = 1
    side_len = 2
    yield number
    while number < n:
        for i in range(4):
            number +=side_len
            yield number
            
if __name__ == '__main__':
    print dig(1001)
    print sum((i for i in gen_diag(25)))