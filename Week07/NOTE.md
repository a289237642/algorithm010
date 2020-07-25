###### 红黑树
* [二叉搜索树](https://visualgo.net/zh/bst?slide=1)
1. 概念解析
1.1 左子树上所有节点的值均小于它的根节点的值
1.2 右子树上所有节点的值均大于它的根节点的值
1.3 依次类推：左右子树也分别为二叉搜索树
1.4 中序遍历：升序遍历
2. 常见操作
3. 基本实现
4. 简单分析
* 平衡二叉树
1. 概念解析
1.1 左子树和右子树的深度差（平衡因子）的绝对值不超过 1
1.2 左右子树也分别为平衡二叉树
2. 基本实现
2.1 左旋
2.2 右旋
2.3 左右旋
2.4 右左旋
3. 性能分析
3.1 节点需要存储额外信息
3.2 调整次数频繁
* 红黑树
1. 概念解析
1.1 每个节点要么是红色要么是黑色
1.2 根节点是黑色的
1.2 每个叶节点（NIL 节点/空节点）都是黑色的
1.3 任何相邻的阶段都不能同时为红色
1.4 从任一节点到其每个叶子节点的所有路径都包含相同数目的黑色节点
2. 实现技巧
2.1 把红黑树的平衡调整的过程比作魔方复原
2.2 找准关注节点：不要搞丢、搞错关注节点
2.3 插入操作的平衡调整比较简单而删除操作就比较复杂
3. 适用场景
3.1 解决普通二叉树在频繁插入、删除等动态更新操作时时间复杂度退化问题
3.2 实际工程中更倾向用跳表来替代
* 实战题目
1. [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)
2. [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
###### 字典树
* 概念解析
1. 节点本身不存在完整单词
2. 从根节点到某一节点路径经过的字符串连接起来为该节点对应的字符串
3. 每个节点的所有子节点路径代表的字符都不相同
* 适用场景
1. 统计和排序大量的字符串
2. 搜索引擎词频统计及关键字提醒
* 实战题目
1. [实现 Trie](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)
2. [单词搜索](https://leetcode-cn.com/problems/word-search/)
3. [单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)
###### 并查集
* 概念解析
1. 一种树型数据结构在使用中以森林来表示
2. 用于处理不交集的合并及查询问题
* 常见操作
1. 初始化：把每个点所在的集合测试为其自身 -> O(n)
2. 合并：将两个元素所在的集合合并为一个集合 -> 建立关系
3. 查找：查找元素所在集合（即根节点）
* 优化方式
1. 将 rank 浅的合并到 rank 深的
2. 路径压缩

* 并查集代码模板

```
def init(p):
    # for i = 0 .. n: p[i] = i
    p = [i for i in range(n)]
    
def union(self, p, i, j):
    p1 = self.parent(p, i)
    p2 = self.parent(p, j)
    p[p1] = p2

def parent(self, p, i):
    root = i
    while p[root] != root:
        root = p[root]
    # 路径压缩
    while p[i] != i:
        x = i; i = p[i]; p[x] = root
    return root

```
* 适用场景
1. 帮派识别：小弟 -> 老大
2. 组团配对
* 实战题目
1. [朋友圈](https://leetcode-cn.com/problems/friend-circles/)
2. [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
3. [被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)
###### 搜索算法
* 遍历搜索
1. 每个节点都要访问一次
2. 每个节点仅要访问一次
* 暴力搜索：时间复杂度：O(E)/空间复杂度：O(V)
1. 广度优先搜索（BFS） --> 层层遍历
```
def BFS(graph, start, end):
    """
    1. visited -> 记录已被访问的顶点
    2. queue -> 存储已被访问但相连的顶点还未被访问的顶点
    """
    queue = []
    queue.append([start])
    
    visited = set()
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
        
    # other processing work
    ...
```
2. 深度优先搜索（DFS） -> 回溯思想
```
def DFS(self, tree):
    if tree.root is None: return []
    
    visited, stack = [], []
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
        
    # other processing work
    ...
```
```
def DFS(node, visited):
    visited = set()
    visited.add(node)
    
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            DFS(next_node, visited)
```
* 高级搜索
1. 剪枝
2. 双向搜索
3. 启发式搜索
```
def AstarSearch(graph, start, end):
    """
    1. 启发式函数评价哪些节点最优希望是我们要找的节点的估计成本
    2. 启发式函数是一种告知搜索方向的方法来猜测会导向的一个目标
    """
    # 优先级 -> 估价函数
    pq = collections.priority_queue()
    pq.append([start])
    visited.add(start)
    
    while pq:
        node = pq.pop()
        visited.add(node)
        
        process（node)
        
        nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```
* 实战题目
1. [二叉树最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
2. [二叉树最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
3. [在每个树中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)
4. [扫雷游戏](https://leetcode-cn.com/problems/minesweeper/description/)
5. [括号生成](https://leetcode-cn.com/problems/generate-parentheses/#/description)
6. [单词接龙](https://leetcode-cn.com/problems/word-ladder/description/%0A/)
7. [单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/description/%0A/)
8. [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description)
9. [二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/)
10. [滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle/)
11. [解数独](https://leetcode-cn.com/problems/sudoku-solver/)