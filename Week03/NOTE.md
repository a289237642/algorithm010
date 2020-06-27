学习笔记

**目录**
- [第7课 | 泛型递归、树的递归](#第7课--泛型递归树的递归)
  - [1.知识点](#1知识点)
  - [2.实战题目](#2实战题目)
      - [70. 爬楼梯](#70-爬楼梯)
      - [226. 翻转二叉树](#226-翻转二叉树)
      - [98. 验证二叉搜索树](#98-验证二叉搜索树)
      - [104. 二叉树的最大深度](#104-二叉树的最大深度)
      - [111. 二叉树的最小深度](#111-二叉树的最小深度)
      - [297. 二叉树的序列化与反序列化](#297-二叉树的序列化与反序列化)
      - [236. 二叉树的最近公共祖先](#236-二叉树的最近公共祖先)
      - [105. 从前序与中序遍历序列构造二叉树](#105-从前序与中序遍历序列构造二叉树)
      - [77. 组合](#77-组合)
      - [46. 全排列](#46-全排列)
      - [47. 全排列 II](#47-全排列-ii)
- [第8课 | 分治、回溯](#第8课--分治回溯)
  - [1.知识点](#1知识点-1)
  - [2.实战题目](#2实战题目-1)
      - [22. 括号生成](#22-括号生成)
      - [50. Pow(x, n)](#50-powx-n)
      - [78. 子集](#78-子集)
      - [169. 多数元素](#169-多数元素)
      - [17. 电话号码的字母组合](#17-电话号码的字母组合)
      - [51. N皇后](#51-n皇后)


# 第7课 | 泛型递归、树的递归

## 1.知识点



## 2.实战题目

#### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

> 假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。
>
> 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
>
> **注意：**给定 *n* 是一个正整数。
>
> **示例 1：**
>
> ```
> 输入： 2
> 输出： 2
> 解释： 有两种方法可以爬到楼顶。
> 1.  1 阶 + 1 阶
> 2.  2 阶
> ```
>
> **示例 2：**
>
> ```
> 输入： 3
> 输出： 3
> 解释： 有三种方法可以爬到楼顶。
> 1.  1 阶 + 1 阶 + 1 阶
> 2.  1 阶 + 2 阶
> 3.  2 阶 + 1 阶
> ```

**代码实现**

```python3
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

```



#### [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)

> 翻转一棵二叉树。
>
> **示例：**
>
> 输入：
>
> ```
>      4
>    /   \
>   2     7
>  / \   / \
> 1   3 6   9
> ```
>
> 输出：
>
> ```
>      4
>    /   \
>   7     2
>  / \   / \
> 9   6 3   1
> ```
>
> **备注:**
>  这个问题是受到 [Max Howell ](https://twitter.com/mxcl)的 [原问题](https://twitter.com/mxcl/status/608682016205344768) 启发的 ：
>
> > 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

**代码实现**

```Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```



#### [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)

> 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
>
> 假设一个二叉搜索树具有如下特征：
>
> - 节点的左子树只包含**小于**当前节点的数。
> - 节点的右子树只包含**大于**当前节点的数。
> - 所有左子树和右子树自身必须也是二叉搜索树。
>
> **示例 1:**
>
> ```
> 输入:
>     2
>    / \
>   1   3
> 输出: true
> ```
>
> **示例 2:**
>
> ```
> 输入:
>     5
>    / \
>   1   4
>      / \
>     3   6
> 输出: false
> 解释: 输入为: [5,1,4,null,null,3,6]。
>      根节点的值为 5 ，但是其右子节点值为 4 。
> ```

**解题思路**

自顶向下的思路，对于左子树左结点来说，其值小于所有祖先结点的值，对于右结点来说，其值大于所有祖先结点，那么对于任意结点，其值都有一个范围 `[left,right]`即 `left  < val < right`

对于树根结点，我们可以一开始初始化  `left = -INF ,right = INF`

当从父结点向下时，左孩子的数值范围就变为  `left < val < father`  ，

右孩子的数值范围就变为  `father < val < right`,

可以一直递归向下 要么不满足条件中途返回false回溯回到根节点，要么遍历完所有的结点返回true

**代码实现**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left and not self.traverse(root.left, float('-inf'), root.val):
            return False
        if root.right and not self.traverse(root.right, root.val, float('inf')):
            return False
        return True

    def traverse(self, node, lower, upper):
        if node.val <= lower or node.val >= upper:
            return False
        if node.left and not self.traverse(node.left, lower, node.val):
            return False
        if node.right and not self.traverse(node.right, node.val, upper):
            return False
        return True
```



#### [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

> 给定一个二叉树，找出其最大深度。
>
> 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
>
> **说明:** 叶子节点是指没有子节点的节点。
>
> **示例：**
> 给定二叉树 `[3,9,20,null,null,15,7]`，
>
> ```
>  3
> / \
> 9  20
>  /  \
> 15   7
> ```
>
> 返回它的最大深度 3 。

**代码实现**

```Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l_depth = self.maxDepth(root.left)
            r_depth = self.maxDepth(root.right)
            return max(l_depth,r_depth)+1

```



#### [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

> 给定一个二叉树，找出其最小深度。
>
> 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
>
> **说明:** 叶子节点是指没有子节点的节点。
>
> **示例:**
>
> 给定二叉树 `[3,9,20,null,null,15,7]`,
>
> ```
>  3
> / \
> 9  20
>  /  \
> 15   7
> ```
>
> 返回它的最小深度  2.

**代码实现**

```Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([(root,1)])
        while q:
            n,l = q.popleft()
            if n.left is None and n.right is None:
                return l
            else:
                if n.left:
                    q.append((n.left,l+1))
                if n.right:
                    q.append((n.right,l+1))
```



#### [297. 二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)

> 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
>
> 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
>
> **示例:** 
>
> ```
> 你可以将以下二叉树：
> 
>     1
>    / \
>   2   3
>      / \
>     4   5
> 
> 序列化为 "[1,2,3,null,null,4,5]"
> ```
>
> **提示:** 这与 LeetCode 目前使用的方式一致，详情请参阅 [LeetCode 序列化二叉树的格式](https://leetcode-cn.com/faq/#binary-tree)。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
>
> **说明:** 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。

**解题思路**

序列化和反序列化之间的约定：二叉树的前序遍历/中序遍历/后序遍历/层次遍历

序列化：按遍历约定遍历二叉树，将空结点记为字符“n”,并用字符“,”作为分隔符，分隔每个结点的值

反序列化：先将序列化的字符串分割成单个结点值到容器中，顺序遍历容器，同时按二叉树的遍历约定递归建立二叉树

**实现细节**


```Python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
from  collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None: 
            return  ''
        q = deque([(root)]) 
        l = []
        while q:
            n = q.popleft()
            if n != None:
                q.append(n.left)
                q.append(n.right)
                l.append(str(n.val))
            else:
                l.append('Null')

        return ' '.join(l)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '': return None
        array = data.split(' ')
        root = TreeNode(int(array[0]))
        q = deque([root])
        index = 1
        while q:
            n = q.popleft()
            if array[index] != 'Null':
                n.left = TreeNode(int(array[index]))
                q.append(n.left)
            index += 1
            if array[index] != 'Null':
                n.right = TreeNode(int(array[index]))
                q.append(n.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

#### [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

> 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
>
> [百度百科](https://baike.baidu.com/item/最近公共祖先/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”
>
> 例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]
>
> ![img](%E7%AC%AC%E4%B8%89%E5%91%A8%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.assets/binarytree.png)
>
> **示例 1:**
>
> ```
> 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
> 输出: 3
> 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
> ```
>
> **示例 2:**
>
> ```
> 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
> 输出: 5
> 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
> ```
>
> **说明:**
>
> - 所有节点的值都是唯一的。
> - p、q 为不同节点且均存在于给定的二叉树中

**解题思路**

先递归遍历查找结点p和q，遍历的过程中用vector记录下他们各自经过的路径上的结点。

顺序比较p,q的vector，直到遇到val值不同，那么最后一个相同的结点即是他们的最近公共祖先

复杂度分析：递归遍历查找结点，每个结点只会被遍历一次，复杂度O(n)；分别查找两次结点，再加上一次顺序比较vector，总的时间复杂度为 O(n)+ O(n)+ O(n) =  O(n)

**代码实现**

```Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        def dfs(n, path):
            if n:
                path.append(n)
                if n in (p, q):
                    ans.append(list(path))   # must use list, or you will get []
                    if len(ans) == 2:		 # optimized
                        return 
                dfs(n.left, path)
                dfs(n.right, path)
                path.pop()
        dfs(root, [])
        return next(a for a, b in list(zip(*ans))[::-1] if a==b)

```



#### [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

> 根据一棵树的前序遍历与中序遍历构造二叉树。
>
> **注意:**
>  你可以假设树中没有重复的元素。
>
> 例如，给出
>
> ```
> 前序遍历 preorder = [3,9,20,15,7]
> 中序遍历 inorder = [9,3,15,20,7]
> ```
>
> 返回如下的二叉树：
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```

**解题思路**

把前序遍历数组中的每个值作为一个子树的root，对于前序遍历数组中任意一个root，到中序遍历中寻找此root，根据root的位置，将中序遍历数组划分为3段，其中 [ inleft , index(root)-1 ]部分作为此root的左子树， [ index(root)+1,inright ] 部分作为此root的左子树 ，而此时左子树的结点个数 为 index(root)-inleft,所以当递归向下进入左子树时，其根的范围在前序遍历中变为 [ preleft + 1,preleft +  index(root)-left ]

递归终止的条件就是 ( preleft > preright \| | inleft > inright ) ,返回NULL，回到上次层就会作为空的左孩子或者右孩子

**代码实现**

```Python3
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
        # pi, pj: the start and end of preorder array
        # ii, ij: the start and end of inorder array
        
        if pi == pj:
            return TreeNode(self.preorder[pi])
        if pi > pj:
            return None
        
        root_val = self.preorder[pi]
        # rest of preorder: pi+1, pj
    
        root = TreeNode(root_val)
        pivot = self.inorder_index[root_val]
        
        # number of nodes in left: pivot-ii
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
        
```



#### [77. 组合](https://leetcode-cn.com/problems/combinations/)

> 给定两个整数 *n* 和 *k*，返回 1 ... *n* 中所有可能的 *k* 个数的组合。
>
> **示例:**
>
> ```
> 输入: n = 4, k = 2
> 输出:
> [
>       [2,4],
>       [3,4],
>       [2,3],
>       [1,2],
>       [1,3],
>       [1,4],
> ]
> ```

**代码实现**

```Python3
/*
	     1  2  3  4
-----------------------------------------------
		 1                 2          3
	2      3    4       3    4        4 
 3   4     4            4 
*/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        
        if n == k:
            return [list(range(1,n+1))]
        
        return_list = []
        self._generate_combinations(1, [], return_list, n, k)
        
        return return_list
    
    def _generate_combinations(self, start_index, current_list, return_list, n, k):
        if len(current_list) == k:
            return_list.append(current_list)
            return
        
        for i in range(start_index, n+1):
            self._generate_combinations(i + 1, current_list + [i], return_list,
                                   n, k)
```



#### [46. 全排列](https://leetcode-cn.com/problems/permutations/)

> 给定一个 **没有重复** 数字的序列，返回其所有可能的全排列。
>
> **示例:**
>
> ```
> 输入: [1,2,3]
> 输出:
> [
>   [1,2,3],
>   [1,3,2],
>   [2,1,3],
>   [2,3,1],
>   [3,1,2],
>   [3,2,1]
> ]
> ```

**代码实现**

```Python3
/*
           1                         2                                 3
  1        2       3      |   1      2        3         |      1       2        3
1 2 3    1 2 3   1 2 3      1 2 3   1 2 3    1 2 3           1 2 3   1 2 3    1 2 3 

*/

class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          
    
    """
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
```



#### [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

> 给定一个可包含重复数字的序列，返回所有不重复的全排列。
>
> **示例:**
>
> ```
> 输入: [1,1,2]
> 输出:
> [
>   [1,1,2],
>   [1,2,1],
>   [2,1,1]
> ]
> ```

**解题思路**

相比【全排列】这题，【全排列II】中含有重复元素，但是输出的排列不能含有重复的排列。

可以对原始数组先进行排序，这样相同的元素都集中到一起了，对于递归的每层，重复的排列的特征是：

这个元素和前一个元素相等，并且前一个元素没有在原始数组中被使用过(保证了这两个相同的数是同层的)。

`if(i>0 && orgNums[i] == orgNums[i-1] && !used[i-1])`

我们只需要遇到这样的重复排列时，循环跳过即可

**代码实现**

```Python3
/*
           1                         1                             2
  1        1       2      |   1      1        2       |     1      1       2
1 1 2    1 1 2   1 1 2      1 1 2   1 1 2     1 1 2       1 1 2   1 1 2    1 1 2

*/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def dfs(path=[], rest=nums):
            if not rest:
                res.append(path)
            else:
                 for i in range(len(rest)):
                     if i > 0 and rest[i] == rest[i-1]: continue # skip duplicate
                     dfs(path+rest[i:i+1], rest[:i]+rest[i+1:])
        dfs()
        return res
```





# 第8课 | 分治、回溯

## 1.知识点
### 分治
分治最典型就是mergySort了，这个排序算法是在学习排序的时候必学的，用到就是分治思想。

什么样的问题适合用分治思想解决？那么就是如下几点：

一个大问题可以拆解程若干小问题。
每个小问题可以再拆解或者到达终止条件。例如说mergy算法，最终拆解到只剩一个元素，到达了终止条件。
每个小问题各不相同，如果小问题都相同。
小问题处理完后能合并回原来的整体。
为什么要强调如上几个点，就是为了和动态规划、回溯、贪婪算法区分开来。这几种算法的特点等会在下面说。一个明显的不同就是后者存在相同的子问题，可以将相同的子问题缓存下来，避免多次计算。

**代码实现**

```Python3
def divide_and_conquer(datas, paras):
    if exit_condition(datas): #终止条件
        return
    subData = split_data(datas)  #问题可被分解为不同的子问题
    result1 = divide_and_conquer(subdata[0], paras)
    result2 = divide_and_conquer(subdata[1], paras)
    result3 = divide_and_conquer(subdata[2], paras)
    ...
    result = mergy_data(result1, result2. result3...) #问题的结果可被还原为整体
    return result
```

 
### 回溯
回溯是一种暴力算法，如果需要用到遍历，那么就使用回溯。例如说alphago围棋，最简单容易想到的就是回溯暴力计算了，为了推测下一步走那个子胜率高，我们对于可能下的位置的点用回溯遍历计算出一个概率，然后选择胜率最高的位置放下一个子。但是对于围棋，需要超出人类想象的计算能力和存储能力才能用暴力计算完成，所以说需要用不同的算法优化等。

上述对于alphago的回溯计算也就说明了回溯算法的优缺点：

优点是容易想到
缺点是只能面对小数据集，使用面有限。
进而下一步的，如果想用回溯算法，需要进行优化。例如说在树和图的深度优先的回溯中，有个比较专门的优化名词，剪枝，也就是将一些不需要的路径给剪掉，从而减少计算量。

**代码实现**

```Python3
def backtracking(level, paras):
    if exist_condition(level):
        return
    state = keepsate(level)  #保存当前状态
    backtracking(level+1, paras):
    reverseState(level, state) #恢复当前状态
```





## 2.实战题目

#### [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

> 数字 *n* 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。
>
> **示例：**
>
> ```
> 输入：n = 3
> 输出：[
>        "((()))",
>        "(()())",
>        "(())()",
>        "()(())",
>        "()()()"
>      ]
> ```

**代码实现**

```Python3
/*
方法一还有改进的余地：我们可以只在序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，

如果左括号数量不大于 nnn，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。

*/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def fn(s, op, cl):
            """Backtracking to collect parentheses"""
            if cl == n: return ans.append(s)
            if op <  n: fn(s+"(", op+1, cl)
            if cl < op: fn(s+")", op, cl+1)
                
        ans = []
        fn("", 0, 0)
        return ans 


```



#### [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)

> 实现 [pow(*x*, *n*)](https://www.cplusplus.com/reference/valarray/pow/) ，即计算 x 的 n 次幂函数。
>
> **示例 1:**
>
> ```
> 输入: 2.00000, 10
> 输出: 1024.00000
> ```
>
> **示例 2:**
>
> ```
> 输入: 2.10000, 3
> 输出: 9.26100
> ```
>
> **示例 3:**
>
> ```
> 输入: 2.00000, -2
> 输出: 0.25000
> 解释: 2-2 = 1/22 = 1/4 = 0.25
> ```
>
> **说明:**
>
> - -100.0 < *x* < 100.0
> - *n* 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

**代码实现**

```Python3

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        power = 1
        current_product = x
        while n > 0:
            # if n is odd numberm, we need to time x one more time
            if n%2 : 
                power = power * current_product
            current_product = current_product * current_product
            n = n//2
        return power

```



#### [78. 子集](https://leetcode-cn.com/problems/subsets/)

> 给定一组**不含重复元素**的整数数组 *nums*，返回该数组所有可能的子集（幂集）。
>
> **说明：**解集不能包含重复的子集。
>
> **示例:**
>
> ```
> 输入: nums = [1,2,3]
> 输出:
> [
>   [3],
>   [1],
>   [2],
>   [1,2,3],
>   [1,3],
>   [2,3],
>   [1,2],
>   []
> ]
> ```

**代码实现**

```Python3
class Solution:
    """
    level 0: []
    level 1: [11]                    [22]       [33]
    level 2: [11,22]     [11,33]     [22,33] 
    level 3: [11,22,33]
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(res,0,[],nums)
        return res
    def backtracking(self,res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
            subset.append(nums[i])
            self.backtracking(res,i+1,subset,nums)
            subset.pop()

```



#### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

> 给定一个大小为 *n* 的数组，找到其中的多数元素。多数元素是指在数组中出现次数**大于** `⌊ n/2 ⌋` 的元素。
>
> 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
>
> **示例 1:**
>
> ```
> 输入: [3,2,3]
> 输出: 3
> ```
>
> **示例 2:**
>
> ```
> 输入: [2,2,1,1,1,2,2]
> 输出: 2
> ```

**代码实现**

```Python3
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]

```



#### [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

> 给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。
>
> 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
>
> <img src="%E7%AC%AC%E4%B8%89%E5%91%A8%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.assets/17_telephone_keypad.png" alt="img" style="zoom:50%;" />
>
> **示例:**
>
> ```
> 输入："23"
> 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
> ```
>
> **说明:**
>  尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

**代码实现**

```Python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        self.mapping = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        self.backtracking(res,[],0,digits)
        return res
    def backtracking(self,res,subset, index,digits):
        if len(digits) == index:
            res.append(''.join(subset))
            return 
        for i in self.mapping[digits[index]]:
            subset.append(i)
            self.backtracking(res,subset,index+1,digits)
            subset.pop()
```



#### [51. N皇后](https://leetcode-cn.com/problems/n-queens/)

> *n* 皇后问题研究的是如何将 *n* 个皇后放置在 *n*×*n* 的棋盘上，并且使皇后彼此之间不能相互攻击。
>
> <img src="%E7%AC%AC%E4%B8%89%E5%91%A8%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.assets/8-queens.png" alt="img"  />
>
> 上图为 8 皇后问题的一种解法。
>
> 给定一个整数 *n*，返回所有不同的 *n* 皇后问题的解决方案。
>
> 每一种解法包含一个明确的 *n* 皇后问题的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。
>
> **示例:**
>
> ```
> 输入: 4
> 输出: [
>  [".Q..",  // 解法 1
>   "...Q",
>   "Q...",
>   "..Q."],
> 
>  ["..Q.",  // 解法 2
>   "Q...",
>   "...Q",
>   ".Q.."]
> ]
> 解释: 4 皇后问题存在两个不同的解法。
> ```
>
> **提示：**
>
> - **皇后**，是[国际象棋](https://baike.baidu.com/item/国际象棋)中的棋子，意味着[国王](https://baike.baidu.com/item/国王)的妻子。皇后只做一件事，那就是“[吃子](https://baike.baidu.com/item/吃子)”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 [百度百科 - 皇后](https://baike.baidu.com/item/皇后/15860305?fr=aladdin) ）

**代码实现

```Python3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []
        def backtrack(pos, row):
            if len(pos) == n and row == n:
                sols.append(pos)
            for col in range(n):
                if all(row != row1 and col != col1 and abs(row - row1) != abs(col - col1)
                        for row1, col1 in pos):
                    backtrack(pos + [(row, col)], row + 1)
        backtrack([], 0)
        return [
            [''.join('Q' if (i, j) in sol else '.' for i in range(n)) for j in range(n)]
            for sol in sols
        ]
```

