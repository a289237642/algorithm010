
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树:

返回其后序遍历: [5, 6, 3, 2, 4, 1].

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return res

        def recursion(root, res):
            for child in root.children:
                recursion(child.res)
            res.append(root.val)

        recursion(root, res)
        return res
