# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:32:20 2017

@author: mmakwana
"""
import math
count = 0
max_value = (0,0)
with open('p099_base_exp.txt') as f:
    for i in f:
        count +=1
        value = map(int, i.replace("\n","").split(","))
        current_value = value[1]*math.log(value[0])
        if current_value > max_value[0]:
            max_value = (current_value, count)
            print max_value
print "Answer is: " + str(max_value[1])