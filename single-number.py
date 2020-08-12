# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:19:24 2020

@author: kamyar
"""

def singleNumber(nums) -> int:
    single = nums[0]
    for i in range(1,len(nums)):
        single = single ^ nums[i]
        print(single)
    return single

print(singleNumber([2,6,7,2,6,8,7]))    


