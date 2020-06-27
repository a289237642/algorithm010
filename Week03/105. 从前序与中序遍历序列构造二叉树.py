"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    
    def __init__(self):
        self.inorder_index = {}
        self.preorder = []
        self.inorder = []
        self.n = 0
    
    def build(self, pi, pj, ii, ij):
        
        
        if pi == pj:
            return TreeNode(self.preorder[pi])
        if pi > pj:
            return None
        
        root_val = self.preorder[pi]
        
    
        root = TreeNode(root_val)
        pivot = self.inorder_index[root_val]
        
        
        root.left = self.build(pi+1, pi+pivot-ii, ii, pivot-1)
        root.right = self.build(pi+1+pivot-ii, pj, pivot+1, ij)
        
        return root
        
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        self.n = len(preorder)
        if not self.n: return None
        
        self.preorder = preorder 
        for i,e in enumerate(inorder):
            self.inorder_index[e] = i
        
        return self.build(0, self.n-1, 0, self.n-1)