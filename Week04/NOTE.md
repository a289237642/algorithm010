### 深度优先搜索属于图算法的一种，英文缩写为DFS即Depth First Search.其过程简要来说是对每一个可能的分支路径深入到不能再深入为止，而且每个节点只能访问一次.
### DFS 代码模板
## 递归写法 ##
```Python3
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)



## 非递归写法 ## 
```Python3
def DFS(self, tree): 
	if tree.root is None: 
		return [] 
	visited, stack = [], [tree.root]
	while stack: 
		node = stack.pop() 
		visited.add(node)
		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 
	# other processing work 
	...
```
### 宽度优先搜索算法（又称广度优先搜索）是最简便的图的搜索算法之一，这一算法也是很多重要的图的算法的原型。Dijkstra单源最短路径算法和Prim最小生成树算法都采用了和宽度优先搜索类似的思想。其别名又叫BFS，属于一种盲目搜寻法，目的是系统地展开并检查图中的所有节点，以找寻结果。换句话说，它并不考虑结果的可能位置，彻底地搜索整张图，直到找到结果为止。
### BFS 代码模板

```Python3
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

### 贪心的实现、特性
### 贪心算法（又称贪婪算法），在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的仅是在某种意义上的局部最优解。贪心算法不是对所有问题都能得到整体最优解，但对范围相当广泛的许多问题他能产生整体最优解或者是整体最优解的近似解。

### 特性：
（1）贪心选择性质
（2）最优子结构性质
## 2.实战题目

#### [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)
**代码实现**

```python3
贪心
1. 想要总硬币数最少，肯定是优先用大面值硬币，所以对 coins 按从大到小排序
2. 先丢大硬币，再丢会超过总额时，就可以递归下一层丢的是稍小面值的硬币

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return - 1
        dp = [[amount + 1 for _ in range(len(coins) + 1)]
              for _ in range(amount + 1)]
        # 初始化第一行为0，其他为最大值（也就是amount + 1）

        for j in range(len(coins) + 1):
            dp[0][j] = 0

        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                if i - coins[j - 1] >= 0:
                    dp[i][j] = min(
                        dp[i][j - 1], dp[i - coins[j - 1]][j] + 1)
                else:
                    dp[i][j] = dp[i][j - 1]

        return -1 if dp[-1][-1] == amount + 1 else dp[-1][-1]


```

## 二分查找代码模板 ##
```Python3
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```

### 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

```Python3
【基本思路】

　　尽可能的利用二分查找，但是最坏情况仍然无法避免O(N)的时间复杂度。首先需要知道，如果一个有序数组经过旋转后，只有一个位置会出现降序，其余部分都是升序。同时，数组的第一个元素一定比最后一个元素大。如果没有经过旋转，数组整体都是升序。在有序数组中找一个数可以利用二分法。

　　所以在利用二分查找的时候，在arr[left] != arr[mid]的情况下，如果arr[left] < arr[mid]，说明arr[left…mid]是有序的，如果n大于arr[left]并且小于arr[mid]，说明n在左半区，令right = mid-1；如果n不在arr[left…mid]区间，则一定在右半区，令left = mid+1。

　　同理，在arr[mid] != arr[right]的情况下，如果arr[mid] < arr[right]，说明arr[mid…right]是有序的，如果n大于arr[mid]并且小于arr[right]，说明n在右半区，令left = mid+1；如果n不在arr[mid…right]区间，则一定在左半区，令right = mid-1。

　　通过上面分析我们可以知道，只要arr[left]、arr[mid]、arr[right]不都相同的时候，二分就可以进行。

　　但是有一个很重要的问题，在arr数组中可能存在重复的值，那么就可能发生arr[left] == arr[mid] == arr[right]的情况。这个时候，我们从left位置开始，向右遍历，直到arr[left] != arr[mid]。如果遍历到mid位置都一直与arr[mid]相等，说明左半区都是一个值，所以n一定出现在右半区，所以令left = mid + 1。

　　最坏的情况下，所有的值都是一个值。对于每个值都需要遍历一遍，所以最坏的时间复杂度是O(N)。


def isContains(arr, num):
    if arr == None or len(arr) == 0:
        return False
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return True
        if arr[left] == arr[mid] == arr[right]:
            while left < mid and arr[left] == arr[mid]:
                left += 1
            if left == mid:
                left = mid + 1
                continue
        if arr[left] != arr[mid]:
            if arr[left] < arr[mid]:
                if num < arr[mid] and num >= arr[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if num > arr[mid] and num <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            if arr[mid] < arr[right]:
                if num > arr[mid] and num <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if num >= arr[left] and num < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
    return False


```


## 2.实战题目

#### [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)
```Python3
class Solution:
    def mySqrt(self, x: int) -> int:
        # 为了照顾到 0 把左边界设置为 0
        left = 0
        # 为了照顾到 1 把右边界设置为 x // 2 + 1
        right = x // 2 + 1
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left

```