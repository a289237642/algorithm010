
# 学习笔记

## 7 种常见的时间复杂度 Big O Notation
	* O(1): Constant Complexity 常数时间复杂度
	* O(log n): Logarithmic Complexity 对数复杂度
	* O(n): Linear Complexity 线性时间复杂度
	* O(n^2): N square Complexity 平方
	* O(n^3): N square Complexity 立方
	* O(2^n): Exponential Growth 指数
	* O(n!): Factorial 阶乘

## 常识
    * 二叉树数的前中后序遍历的时间复杂度---O(N)
    * 图的遍历的时间复杂度---O(N)
    * 索索算法(DFS、BFS)的时间复杂度---O(N)
    * 二分查找的时间复杂度---O(logN)

## 跳表的特点
### 注意：只能用于元素有序的情况。
	* 所以，跳表（skip list）对标的是平衡树（AVL Tree）和二分查找，是一种 插入/删除/搜索 都是 O(log n) 的数据结构。1989 年出现。

	* 它最大的优势是原理简单、容易实现、方便扩展、效率更高。在一些热门的项目里用来替代平衡树，如 Redis、LevelDB 等。

## 跳表查询的时间复杂度分析
   * n/2、n/4、n/8、第 k 级索引结点的个数就是 n/(2^k)
假设索引有 h 级，最高级的索引有 2 个结点。n/(2^h) = 2，从而求得 h = 
log2(n)-1

## 跳表的空间复杂度分析
	* 原始链表大小为 n，每 2 个结点抽 1 个，每层索引的结点数： n/2 , n/4 , n/8 , ⋯ , 8,4,2
	* 原始链表大小为 n，每 3 个结点抽 1 个，每层索引的结点数： n/3 , n/9 , n/27 , ⋯ , 9,3,1
	空间复杂度是 O(n)


## Stack & Queue 关键点
	* Stack：先入后出；添加、删除皆为 O(1)

	* Queue：先入先出；添加、删除皆为 O(1)

