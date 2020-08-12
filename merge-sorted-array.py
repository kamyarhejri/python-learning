# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 23:27:23 2020

@author: kamyar
"""

a = []
b = []

#one easy way
#c = a + b
#print(sorted(c))

#second way: implementing my own function to perform the task
def mergesort(x,y):
  result = []
  i = 0
  j = 0
 
  if len(x) == 0 and len(y) == 0:
      print("invalid inputs!")
      return []
  elif len(x) == 0:
      return y
  elif len(y) == 0:
      return x
  else:
      while i<len(x) and j<len(y):
          if x[i] < y[j]:
              result.append(x[i])
              i+=1
          else:
              result.append(y[j])
              j+=1
      while i<len(x):
          result.append(x[i])
          i+=1
      while j<len(y):
          result.append(y[j])
          j+=1     
  return result

d = mergesort(a,b)
print(d)