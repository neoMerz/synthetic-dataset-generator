# - * - coding: utf-8 - * - 
"""
Binary Tree
This module creates simple binary trees.

Authors: 
    Nicolò Merzi
    Francesco Battista

"""
import random
from random import shuffle

class BinaryTree:
    """Class Bynary Tree is used to create a binary tree. 
    It's built as node serie, the root node rapresents the entire tree.
        Methods:
            * get_data()
            * get_parent()
            * get_left()
            * get_right()
            * insertTraversal(self, value)
            * __insertTraversalLeft(self, value) ** Private method
            * __insertTraversalRight(self, value) ** Private method
            * records(self)
            * insertBottom
            * insertHead
    """
    #INITIALIZER
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    #GETTER
    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    #METHODS
    def __str__(self):
        """Overriding string method
        """
        def str_branches(node, branches):
            strings = [str(node.data)]
            i = 0
            if node.left != None or node.right != None:
                for current in [node.left, node.right]:
                    if i == 0:
                        joint = '|-'
                    else:
                        joint = '|_'

                    strings.append('\n')
                    for b in branches:
                        strings.append(b)
                    strings.append(joint)
                    if i == 0:
                        branches.append('|')
                    else:
                        branches.append(' ')

                    if current != None:
                        strings.append(str_branches(current, branches))
                    branches.pop()
                    i += 1
            return "".join(strings)

        return str_branches(self, [])

    def insertTraversal(self, value):
        """Taking a value, less than 0.5 insert the value on left, otherwise on right
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if random.random() <= 0.5:
            self.__insertTraversalLeft(value)
        else: 
            self.__insertTraversalRight(value)

    def __insertTraversalLeft(self, value):
        """Taking a value and insert it on the left branch 
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if self.left != None:
            #print('node found. Going down...')
            self.left.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.left = newNode
            newNode.parent = self

    def __insertTraversalRight(self, value):
        """Taking a value and insert it on the right branch 
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if self.right != None:
            #print('node found. Going down...')
            self.right.insertTraversal(value)
        else:
            #print('free edge found. Inserting node.')
            newNode = BinaryTree(value)
            self.right = newNode
            newNode.parent = self

    def insertBottom(self, value):
        """Taking a value and insert it after the last leaf
        
        Arguments:
            value {[int]} -- [Value inside the node]
        """
        if(self.left != None):
            self.left.insertBottom(value)
        if(self.right != None):
            self.right.insertBottom(value)
        if(self.right == None and self.left == None):
            newNode = BinaryTree(value)
            if random.random() > 0.5:
                self.right = newNode
                newNode.parent = self
            else:
                self.left = newNode
                newNode.parent = self

    def insertHead(self, value):
        """Taking a value and insert it as a root
        
        Arguments:
            value {[int]} -- [Value inside the node]
        
        Returns:
            [Binary Tree] -- [New root node]
        """
        newNode = BinaryTree(value)
        if random.random() > 0.5:
            self.parent = newNode
            newNode.right = self
        else:
            self.parent = newNode
            newNode.left = self
        return newNode
