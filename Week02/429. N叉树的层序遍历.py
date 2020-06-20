
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret



# root = [1,null,3,2,4,null,5,6]
# s=Solution()
# print(s.levelOrder(root))