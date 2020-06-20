<a name="SCzCV"></a>
#### [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
二叉树遍历的前、中、后序递归写法，一定要背熟。
```python
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root,res)
        return res


    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
```
**复杂度分析**<br />**时间复杂度：O(N)**<br />**空间复杂度：O(N)**<br />


#### [N叉树的前、后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
有别于二叉树，N叉树在结构方面则没有left，right节点的。而是统一为children节点
```python
def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
```

<br />调用递归函数时，递归函数内部则应遍历父节点下面的子节点
```python
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:return None
        self.helper(root, res)
        return res

    def helper(self, root, res):
        # res.append(root.val)前序遍历
        for node in root.children:
            self.helper(node, res)
        res.append(root.val)# 后序遍历
```
复杂度分析：<br />• **时间复杂度**：O(n)<br />• **空间复杂度**：O(n)<br />


<br />调用递归函数时，递归函数内部则应遍历父节点下面的子节点
```python
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:return None
        self.helper(root, res)
        return res

    def helper(self, root, res):
        # res.append(root.val)前序遍历
        for node in root.children:
            self.helper(node, res)
        res.append(root.val)# 后序遍历
```
复杂度分析：<br />• **时间复杂度**：O(n)<br />• **空间复杂度**：O(n)<br />


<a name="jR2wt"></a>
#### [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
这道题上周我们是通过双端队列来做的，学了“堆”之后，也是可以使用堆来做的，python中实现的堆，是小顶堆，所以对于求最小最大，要灵活运用 相反数 来求解。<br />
<br />这道题用双端队列来实现，时间复杂度是O(n)，空间复杂度是O(k)，利用堆来实现，时间复杂度是O(nlogn)，空间复杂度是O（n）,所以还是双端队列的实现方式要优于堆实现。
```python
        res, heap = [], []
		for i in range(len(nums)):
			heapq.heappush(heap, ( -nums[i], i))
			if i + 1 >= k:
				while heap and heap[0][1] <  i + 1 - k:
					heapq.heappop(heap)
				res.append(-heap[0][0])
		return res
```



