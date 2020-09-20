# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:30:26 2020

@author: kamyar
"""
import sys
    
def mergesort(x,y):
  result = []
  pairs = []
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
              pairs.append((x[i],y[j]))
              i+=1
          else:
              result.append(y[j])
              pairs.append((y[j],x[i]))
              j+=1
      while i<len(x):
          result.append(x[i])
          i+=1
      while j<len(y):
          result.append(y[j])
          j+=1     
  return result, pairs


a = []
b = []
flag = False
for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    for l in line.rstrip():
        if l == ';':
            flag = True
            continue
        if not flag and l != ',':
            a.append(l)
        else:
            if l != ',':
                b.append(l)

    if a != [] and b != []:
        print(a)
        print(b)
        r, p = mergesort(a,b)
        print(r)
        print(p)
        a.clear()
        b.clear()
    else:
        continue



