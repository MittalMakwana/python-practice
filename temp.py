# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

class sysstat(object):
    '''
    open a sysstat and creat its drive structure
    '''
    drives = {}
    
    def __init__ (self, file):
        self.file = file

driveCaps = {
   'B'  : 1e1,
   'KB' : 1e3,
   'MB' : 1e6,
   'GB' : 1e9,
   'TB' : 1e12,
   'PB' : 1e15
   }

def inodesToint(n):
    n = n.split(' ')
    n = filter(None, n)
    if n[-1] == 'K':
        return float(n[0])*1000
    elif n[-1] == 'M':
        return float(n[0])*1000000
    else:
        return float(n[0])

def capToBytes(n):
    size = n.split(" ")
    return (float(size[0]) * driveCaps[size[1]])
lastcommand = ''
drive = {}
names = []
reDrive = "\A(\S+)\s+(\S+)\s+(\S+)\s+([\d.]*\s*(?:B|KB|MB|GB|TB|-)) \
\s+([\d.]*\s*(?:B|KB|MB|GB|TB|-))\s+([\d.]*\s*(?:B|KB|MB|GB|TB|-))\s+([\d.]+\s?\S*)\s+([\d.]+\s?\S*)"

def process(line):
    if lastcommand == 'sysstat drives' and ( re.search(r"ad\d", line)):
        m = re.compile(reDrive).split(line)
        if m[1] not in drive:
            drive[m[1]] = {}
        # Stores in a list as Total Capacity, Data Spaced used, Metadata Spaced Used, Free Space, Total Inodes    
        drive[m[1]][m[2]] = [capToBytes(m[4]),capToBytes(m[5]),capToBytes(m[6]),capToBytes(m[7]),inodesToint(m[8])]       

with open('sysstat') as f:
    for line in f:
        if 'command: sysstat errors' in line:
            lastcommand = 'sysstat errors'
        if 'command: sysstat drives' in line:
            lastcommand = 'sysstat drives'
        process(line)


print drive