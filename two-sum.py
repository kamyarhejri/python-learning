# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:32:07 2020

@author: kamyar
"""

def twosum(nums, target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            print(required)
            return [required[target - nums[i]],i]
        else:
            required[nums[i]]=i
            print("else:",required)
            
print(twosum([2,8,17,3,5,9],12))
