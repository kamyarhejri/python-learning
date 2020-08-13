# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:55:21 2020

@author: kamyar
"""

a = [2,3,1,1,4,2]

def firstrecurringchar(arr : []):
    d = {}
    if len(arr) < 2:
        return None
    else:
        for i in range(0,len(arr)):
            if arr[i] in d.keys():
                return arr[i]
            else:
                d[arr[i]] = i

print(firstrecurringchar(a))