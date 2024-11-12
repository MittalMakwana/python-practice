# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 17:37:26 2017

@author: mmakwana
"""

words = {
         1: 'one', 
         2: 'two', 
         3: 'three', 
         4: 'four', 
         5: 'five',
         6: 'six', 
         7: 'seven', 
         8: 'eight', 
         9: 'nine', 
         10: 'ten',
         11: 'eleven', 
         12: 'twelve', 
         13: 'thirteen', 
         14: 'fourteen', 
         15: 'fifteen', 
         16: 'sixteen', 
         17: 'seventeen', 
         18: 'eighteen', 
         19: 'nineteen'
         }

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

more = ['hundred', 'thousand']

def n2w(n):
    if 1 <= n <= 19:
        return words[n]
    elif 20 <= n <= 99:
        tenth, below_ten = divmod(n, 10)
        if below_ten == 0: 
            return tens[int(tenth) - 2]
        else:
            return  tens[int(tenth) - 2] + '-' + words[below_ten]
    elif 100 <= n <= 999:
        hundred,ten = divmod(n,100)
        if ten == 0 :
            return words[hundred] + ' ' + more[0]
        else:
            return words[hundred] + ' ' + more[0] + ' and '+n2w(ten)
    elif 1000 <= n <=9999:
        thousand,hund = divmod(n, 1000)
        if hund == 0:
            return words[thousand] + ' ' + more[1]
        else:
            return words[thousand] + ' ' + more[1] + ' ' +n2w(hund)
    else:
        return "invalid number"
    
total = 0
for i in range(1,1001):
    total = total + len(n2w(i).replace(" ", "").replace("-",""))