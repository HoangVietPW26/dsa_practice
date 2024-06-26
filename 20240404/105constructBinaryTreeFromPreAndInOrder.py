from typing import List, Optional
"""
Given two integer arrays preorder and inorder where preorder 
is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        tree = TreeNode(preorder[0])
        partition = inorder.index(preorder[0])
       
        tree.left = self.buildTree(preorder[1:partition+1], inorder[:partition])
        tree.right = self.buildTree(preorder[partition+1:], inorder[partition+1:])
        return tree
        