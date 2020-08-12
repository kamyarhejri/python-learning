# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:02:01 2020

@author: kamyar
"""

class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.data

    def pop(self):
        del self.data[self.length - 1]
        self.length -= 1
        return self.data

    def delete(self, index):
        self.data = self.shift(index)
        return self.data

    def shift(self, index):
        for i in range(index, self.length - 1, 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return self.data


a = MyArray()
a.push('ki')
a.push('hi')
a.push('lo')
a.delete(2)
print(a.data)
