# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:00:11 2017

@author: mmakwana
"""

def test(num):
    prime = [2,3,5,7,11,13,17]
    num_str = str(num)
    for i in range(1, len(num_str) - 2):
        if  int(num_str[i:i+ 3]) % prime[i - 1] != 0 :
            return False
    return True

def is_uniq(n): return len(str(n)) == len(set(str(n)))

def combine(list1, list2):
    for l_1 in list1:
        for l_2 in list2:
            if is_uniq(l_1 + l_2):
                yield l_1 + l_2
    
    
def d8910(): return [str(i).zfill(2) for i in xrange(1,100)]
def d678(): return [str(i) for i in xrange(500,600) if is_uniq(i) and i % 11 ==0 ]

def d345():
    n = []
    for i in xrange(12,1000,3):
        if i < 100 and is_uniq(i) and (i/10)%2 == 0:
             n.append(str(i).zfill(3))
        if is_uniq(i) and "5" not in str(i) and int(str(i)[1]) % 2 == 0 and i > 100:
            n.append(str(i))
    return n

def gen_pandigital():
    def is_uniq(n): return len(str(n)) == len(set(str(n)))
    n = 1023456789
    while n <= 9876543210:
        if is_uniq(n):
            yield n
        n+=1
A0 = [str(i) for i in xrange(10,100) if is_uniq(i)]
A1 = d345()
A2 = d678()
A3 = d8910()
P = combine(combine(A1,A2),A3)
P_l = [i for i in P]
Z = combine(A0,P_l)

print sum(( int(i) for i in Z if test(int(i))))
##a = [i for i in xrange(1023456789,9876543211)]
#a = gen_pandigital()
#for i in a:
#    if test(i):
#        print i