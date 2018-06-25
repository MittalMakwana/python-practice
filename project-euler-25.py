# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 16:54:06 2017

@author: mmakwana
"""

#from project_euler_tool import fibonaci

def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

for index, i in enumerate(fibonacci(10000)):
    if len(str(i)) == 1000:
        print index, i
        break