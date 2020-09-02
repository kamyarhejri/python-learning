# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:39:00 2020

@author: kamyar

Implementing Queue in Python using Stack
"""

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.reversedstack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack:
            self.reversedstack.append(self.stack.pop())
        returnitem = self.reversedstack.pop()
        while self.reversedstack:
            self.stack.append(self.reversedstack.pop())
        return returnitem

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def printqueue(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(' --> ', self.stack[i], end=' ')
        print('\n', end='')

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack:
            return True
        else:
            return False
        
myq = MyQueue()
print("empty? ",myq.empty())
myq.push('Ali')
myq.push('joan')
myq.push('Lili')
myq.printqueue()
myq.pop()
myq.printqueue()
myq.push('Negin')
myq.printqueue()
print("empty? ",myq.empty())
print("Who is next? ",myq.peek())

