# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:48:54 2017

@author: mmakwana
"""

def twoSum(nums, target):
    n = (0,nums[0])
    del nums[0]
    for i in xrange(1, len(nums)):
        print n
        if n[0] + nums[i] == target:
            return n
        else:
            n = (i, nums[0])
            del nums[0]

print twoSum([3, 2, 7, 11, 15],9)