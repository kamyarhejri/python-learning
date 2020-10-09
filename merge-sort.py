# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:08:36 2020

@author: kamyar

Implementation of Merge Sort in Python 3
"""

def mergesort(arr):
    if len(arr) == 1:
        return arr
    else:
        m = len(arr)//2
        left = arr[:m:]
        right = arr[m::]
        mergesort(left)
        mergesort(right)       
        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):            
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr

print(mergesort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
        

