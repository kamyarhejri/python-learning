# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:08:14 2020

@author: kamyar

Implementation of Selection Sort in Python 3

"""

def selectionsort(arr):
    for i in range(0,len(arr),1):
        low = i
        temp = arr[i]
        for j in range(i+1,len(arr),1):
            if arr[j] < arr[low]:
                low = j
        arr[i] = arr[low]
        arr[low] = temp
    return arr
        

print(selectionsort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))