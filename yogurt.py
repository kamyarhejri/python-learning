# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:04:02 2020

@author: kamyar

My solution for a problem in Google Kick Start 2018

Problem:
Lucy loves yogurt, and she has just bought N cups of yogurt, 
but she is worried that she might not be able to consume all 
of them before they expire. The i-th cup of yogurt will expire 
Ai days from today, and a cup of yogurt cannot be consumed on 
the day it expires, or on any day after that.

As much as Lucy loves yogurt, she can still only consume 
at most K cups of yogurt each day. What is the largest number 
of cups of yogurt that she can consume, starting from today?
    
Input format:

The first line of the input gives the number of 
test cases, T. T test cases follow. Each test case
starts with one line containing two integers N and K, 
as described above. Then, there is one more line with 
N integers Ai, as described above.

4
2 1
1 1
5 1
3 2 3 2 3
2 2
1 1
6 2
1 1 1 7 7 7

Output format:
For each test case, output one line containing Case #x: y, 
where x is the test case number (starting from 1) and y is 
the maximum number of cups of yogurt that Lucy can consume, 
as described above.

"""
class yogurt():
    """
    calculate the maximum number of cups of yogurts the Lucy can consume
    """
    def __init__(self, n_bought, k_max_day_dose, expirations):
        self.n_bought = n_bought
        self.k_max_day_dose = k_max_day_dose
        self.expirations = sorted(expirations)
        self.max_consume = 0
    
    def maxcups(self):
        day = 1 #current day
        consumed = 0 # number of cups of yogurt consumed by Lucy in one day
        for i in range(0,self.n_bought):
            # if Lucy consumed the daily dose
            # start the next day
            if consumed == self.k_max_day_dose:
                consumed = 0
                day += 1
            # if yogurt is not expired
            # give it to lucy to consume
            if self.expirations[i] >= day:
                consumed += 1
                self.max_consume += 1
           
        return self.max_consume

# receiving each line of input and process it
t = int(input())
for i in range(1, t+1):
    n_bought , k_max_day_dose = [int(j) for j in input().split()]
    expirations = [int(k) for k in input().split()]
    case = yogurt(n_bought, k_max_day_dose, expirations)
    print("case #{}: {}".format(i, case.maxcups()))


