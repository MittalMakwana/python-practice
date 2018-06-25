# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:36:38 2017

@author: mmakwana
"""
import suduko

class sudoko(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle
    
    def print_puzz(self):
        for i in self.puzzle:
            print i
    

def firtway(txt='p096_sudoku.txt'):
    grid = False
    puzz = ''
    data = []
    with open(txt) as f:
        for i in f:
            line = i.replace("\n","")
            print puzz
            if line.startswith("Grid") : 
                line = ''
                grid = True
            if grid and len(puzz) == 81: 
                data.append(puzz)
                puzz = ''
                grid = False
            else: 
                puzz +=line
        data.append(puzz)
    return data

def second_way(txt='p096_sudoku.txt'):
    data = {}
    with open(txt) as f:
        for l,v in enumerate(f):
            v = v.replace("\n","")
            if l % 10 == 9:
                chunk = map(int, puzz + v)
                data[(l+1)/10] = [chunk[x:x+9] for x in xrange(0,len(chunk),9)]
            elif l % 10  == 0: 
                puzz = ''
            else: puzz +=v
    return data

p = second_way()

for i in p :
    