# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:55:55 2020

@author: kamyar

Implementation of Fibonacci serie using Recursion and Iteration
"""

#Recursion Approach -> O(2^n) not efficient
def fibonacci_rec(n):
  if n<2:
    return n
  else:
    return (fibonacci_rec(n-1) + fibonacci_rec(n-2))

print('recursion: ',fibonacci_rec(15))

#Iteration Approach -> O(n) efficient
def fibonacci_iter(n):
  a = []
  for i in range(0,n+1,1):
    if i < 2:
      a.append(i)
    else:
      a.append(a[i-1]+a[i-2])
  return a[n]

print('iteration: ',fibonacci_iter(40))