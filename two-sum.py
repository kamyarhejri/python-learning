# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:32:07 2020

@author: kamyar
"""

def twosum(nums, target):
    d = {}
    for i in range(0,len(nums)):
        if nums[i] in d.keys():
            return [d[nums[i]],i]
        else:
            d[target-nums[i]] = i
            
print(twosum([6,6],12))
