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
    def __init__ (self, file):
        self.file = file
        self.drives = {}
        self.lastcommand = ''
        self.openfile()
        
        
    def openfile(self):    
        with open(self.file) as f:
            for line in f:
                if 'command: sysstat errors' in line:
                    self.lastcommand = 'sysstat errors'
                if 'command: sysstat drives' in line:
                    self.lastcommand = 'sysstat drives'
                self.process(line)

    def process(self, line):
        if self.lastcommand == 'sysstat drives' and ( re.search(r"ad\d", line)):
            m = re.compile(reDrive).split(line)
            if m[1] not in self.drives:
                self.drives[m[1]] = {}
            # Stores in a list as Total Capacity, Data Spaced used, Metadata Spaced Used, Free Space, Total Inodes    
            self.drives[m[1]][m[2]] = [capToBytes(m[4]),capToBytes(m[5]),capToBytes(m[6]),capToBytes(m[7]),inodesToint(m[8])]


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

def bytestoCap(n):
    
    return 0

reDrive = "\A(\S+)\s+(\S+)\s+(\S+)\s+([\d.]*\s*(?:B|KB|MB|GB|TB|-))\s+([\d.]*\s*(?:B|KB|MB|GB|TB|-))\s+([\d.]*\s*(?:B|KB|MB|GB|TB|-))\s+([\d.]+\s?\S*)\s+([\d.]+\s?\S*)"

def diff(a,b):
    result = {}
    for key in a:
        result[key] = { 
                    'ad0' : [x - y for x, y in zip(a[key]['ad0'], b[key]['ad0'])],
                    'ad2' : [x - y for x, y in zip(a[key]['ad2'], b[key]['ad2'])],
                    'ad4' : [x - y for x, y in zip(a[key]['ad4'], b[key]['ad4'])]
                }
    return result
    
def print_out(drives):
    for key,value in sorted(drives.items()):
        for key2, value2 in sorted(value.items()):
            print key+"\t"+ key2 + "\t" + str(value2[4])
#            print key+"\t"+ key2 + "\t"+ str(value2[0]) + "\t"+ str(value2[1]) \
#            + "\t"+ str(value2[2]) + "\t"+ str(value2[3])

    

a = sysstat('servlet_old.txt')
b = sysstat('servlet_latest.txt')
print_out(diff(a.drives, b.drives))