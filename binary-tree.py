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
            #Left Side
            if not currentnode.left:
               currentnode.left = newnode
               break
            else:
               currentnode = currentnode.left
         else:
            #Right Side
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
     
  def remove(self, value):
    if not self.root:
       print("There is no Tree!")
    else:
       parentnode = None
       currentnode = self.root   
       # finding the node to remove
       while currentnode:
          if value == currentnode.value:
              # we found the node
              # let's cover all different situations to remove 
              # a node in a binary tree:
              #1: node doesn't have any children (easiest case)
              if not currentnode.left and not currentnode.right:
                  # check if the requested node to remove is root
                  if not parentnode:
                      self.root = None
                  else:
                      if parentnode.left == currentnode:
                          parentnode.left = None
                      elif parentnode.right == currentnode:
                          parentnode.right = None
              #2: the node have a right branch only (easy, just reassigning pointers)
              elif not currentnode.left and currentnode.right:
                  if not parentnode:
                      self.root = currentnode.right
                  else:
                      if parentnode.left == currentnode:
                          parentnode.left = currentnode.right
                      elif parentnode.right == currentnode:
                          parentnode.right = currentnode.right
              #3: the node have a left branch only (easy, just reassigning pointers)
              elif currentnode.left and not currentnode.right:
                  if not parentnode:
                      self.root = currentnode.left
                  else:
                      if parentnode.left == currentnode:
                          parentnode.left = currentnode.left
                      elif parentnode.right == currentnode:
                          parentnode.right = currentnode.left 
              #4: the node have both right and left branches (hardest, there are
              # different conditions in this case)
              elif currentnode.left and currentnode.right:
                  # check if the right branch of the node has any left branches
                  child = currentnode.right
                  if child.left:
                  # in this case we loop through left branch to find the smallest leaf
                      smallest = parent = child
                      while smallest:
                          if smallest.left:
                              parent = smallest
                              smallest = smallest.left
                          else:
                              break
                      parent.left = None
                      # then easily remove the smallest leaf in left branch and
                      # and assign its value to the node that we want to remove
                      if not parentnode:
                          self.root.value = smallest.value
                      else:
                          currentnode.value = smallest.value 
                  # if the right branch of the node doesn't have left branches,
                  # we just reassign pointers like previous conditions
                  else: 
                      if not parentnode:
                          holder = self.root
                          self.root = currentnode.right
                          holder.left = currentnode.left
                      else:
                          if parentnode.left == currentnode:
                              parentnode.left = currentnode.right
                              holder = parentnode.left
                              holder.left = currentnode.left
                          elif parentnode.right == currentnode:
                              parentnode.right = currentnode.right
                              holder = parentnode.right
                              holder.left = currentnode.left                          
                  return self.root
          elif value < currentnode.value:
              # if value is smaller than currentnode, go left
              parentnode = currentnode
              currentnode = currentnode.left
          else:
              # if value is bigger than currentnode, go right
              parentnode = currentnode
              currentnode = currentnode.right
       print("There is no node with value {} in this tree!".format(value))       

  def traverse(self, node, arr):
    if node:
      arr.append(node.value)
      arr = self.traverse(node.left, arr)
      arr = self.traverse(node.right, arr)
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
values = tree.traverse(tree.root, [])
print(values)
print(tree.lookup(20))
tree.remove(123)
tree.remove(9)
tree.insert(150)
values = tree.traverse(tree.root, [])
print(values)

