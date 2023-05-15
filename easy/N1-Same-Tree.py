# https://leetcode.com/problems/same-tree/

import random

class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    
class BinaryTree:
    def __init__(self):
        self.root_node = None

    def insert_node(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            self._insert_node(self.root_node, value)
    
    def _insert_node(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)


binary_tree = BinaryTree()

for _ in range(15):
    binary_tree.insert_node(random.randint(1,100))



