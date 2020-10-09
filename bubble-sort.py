# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:48:22 2020

@author: kamyar

Implementation of Bubble Sort in Python 3
"""

def bubblesort(arr):
    for i in range(0,len(arr),1):
        for j in range(i+1,len(arr),1):
            if arr[i] > arr[j]:
                a = arr[j]
                arr[j] = arr[i]
                arr[i] = a
    return arr
                

print(bubblesort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
