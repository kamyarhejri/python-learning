# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:40:01 2020

@author: kamyar

Mining Robot Exercise:

The is a robot in another planet than can mine one gram of mineral per day. it 
can also clone by constructing another robot which takes one day. the robot can 
only perform one task per day; mining mineral or building another robot that can 
mine one gram of mineral per day.

write a program that receives an integer which represents how many grams of mineral
should be mined. the program should calculate the minimum days required to mine n 
grams mineral considering the ability of robot to mine 1 gram per day or build another
robot to help with mining.


"""

import sys

def mindays(n):
    #max possible days with one robot equals n grams of required mineral
    #because it takes one day for the robot to mine one gram mineral
    days = n
    newrecord = 0
    if n == 1:
        return n
    else:
        for extrarobot in range(0, n+1, 1):
            newrecord = int(n/(1 + extrarobot))
            if n%(1 + extrarobot) > 0: 
                newrecord += 1
            newrecord += extrarobot
            days = min(days,newrecord)
        return days

    
for line in sys.stdin:
    try:
        print(mindays(int(line.rstrip())))
    except:
        print("invalid input! Only integer is accepted.")