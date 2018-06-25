# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 20:40:03 2017

@author: mmakwana
"""
def get_word_value(word): return sum((ord(i) - 64 for i in word ))

def convert_file_list(fname):
    with open(fname) as f:
        for line in f:
            return line.replace("\"", "").split(",")

def gen_tri():
    n = 0
    while True:
        n +=1
        yield n*(n+1)/2

tri = lambda n : n*(n+1)/2

T = gen_tri()
WORDS = convert_file_list("p042_words.txt")
WORD_VALUE = [get_word_value(word) for word in WORDS]
TRI = [tri(i) for i in xrange(1,max(WORD_VALUE)) if tri(i)<= max(WORD_VALUE)]
count = 0
for word in WORD_VALUE:
    if word in TRI:
        count +=1
print count