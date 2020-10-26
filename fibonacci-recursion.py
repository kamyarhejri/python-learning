# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:55:55 2020

@author: kamyar

Implementation of Fibonacci serie using:
    1 - Recursion
    2 - Iteration
    3 - Recusrion with Dynamic Programming
"""

cal_r = 0
cal_r_dp = 0
print('calculating nth element in Fibonacci serie using:')


#Recursion Approach -> O(2^n) not efficient
def fibonacci_rec(n):
  global cal_r
  cal_r += 1
  if n<2:
    return n
  else:
    return (fibonacci_rec(n-1) + fibonacci_rec(n-2))

print('recursion: ',fibonacci_rec(15), ' with {} calculations'.format(cal_r))

#Iteration Approach -> O(n) efficient
def fibonacci_iter(n):
  a = []
  for i in range(0,n+1,1):
    if i < 2:
      a.append(i)
    else:
      a.append(a[i-1]+a[i-2])
  return a[n]

print('iteration: ',fibonacci_iter(15))

#Recursion and Dynamic Programming (Memoization) Approach -> O(n) very efficient
def fibonacci_rec_dynamic(n):
  cache = {}
  #using Closure function to avoid defining a global variable for cache
  def dyn_fib(n):
      global cal_r_dp
      cal_r_dp += 1
      if n in cache.keys():
          return cache[n]
      else:         
          if n<2:
             return n
          else:
             cache[n] = (dyn_fib(n-1) + dyn_fib(n-2))
             return cache[n]
  return dyn_fib(n)

fib = fibonacci_rec_dynamic(15)
print('dynamic programming & recursion: ', fib, ' with {} calculations'.format(cal_r_dp))