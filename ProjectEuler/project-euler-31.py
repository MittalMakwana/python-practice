# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 16:00:43 2017

@author: mmakwana
"""

def total_combo(money,final_amount):
    '''
    money = list of denomation of moeny
    final_amount = final_amount to get the total combination
    '''
    # Generate a blank array
    combination = [0 for i in xrange(final_amount+1)]
    combination[0] = 1
    for coin in money:
        for amount in xrange(1,final_amount+1):
            if amount >=coin:
                combination[amount] += combination[amount-coin]
    return combination[-1]


print total_combo([1,2,5,10,20,50,100,200],200)