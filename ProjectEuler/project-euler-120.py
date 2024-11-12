# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 12:23:36 2017

@author: mmakwana
"""

def area(x1,y1,x2,y2,x3,y3):
    return abs((x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2))

def has_origin(x1,y1,x2,y2,x3,y3):
    A = area(x1,y1,x2,y2,x3,y3)
    A1 = area(x1,y1,x2,y2,0,0)
    A2 = area(0,0,x2,y2,x3,y3)
    A3 = area(x1,y1,0,0,x3,y3)
    return A == A1+A2+A3

count = 0
with open('p102_triangles.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        line =  map(int, line.split(","))
        if has_origin(line[0],line[1],line[2],line[3],line[4],line[5]) : count += 1
