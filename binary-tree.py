# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:34:26 2020

@author: kamyar

Implementation of Binary Search Tree in Python
"""

class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree():
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    newnode = Node(value)
    if not self.root:
      self.root = newnode
    else:
      currentnode = self.root     
      while True:
         if value < currentnode.value:
            if not currentnode.left:
               currentnode.left = newnode
               break
            else:
               currentnode = currentnode.left
         else:
            if not currentnode.right:
               currentnode.right = newnode
               break
            else:
               currentnode = currentnode.right

  def lookup(self, value):
    if not self.root:
       return False
    else:
       currentnode = self.root     
       while currentnode:
          if value == currentnode.value:
              return True
          elif value < currentnode.value:
              currentnode = currentnode.left
          else:
              currentnode = currentnode.right
       return False

def traverse(node, arr):
  if node:
    arr.append(node.value)
    arr = traverse(node.left, arr)
    arr = traverse(node.right, arr)
  return arr


#9 4 6 20 170 15 1
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.root.value)
values = traverse(tree.root, [])
print(values)
print(tree.lookup(20))