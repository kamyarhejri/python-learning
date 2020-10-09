# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:01:17 2020

@author: kamyar

Implementation of Insertion Sort in Python
"""

def insertionsort(arr):
    for i in range(0,len(arr),1):
        key = arr[i]
        for j in range(i-1,-1,-1):
            if key < arr[j]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

print(insertionsort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))