学习笔记


###### 动态规划
* 概念解析
动态规划是针对一类求最优解的问题的算法， 其核心是将一个问题分解成为若干个子问题（这里对应下文的子问题使用条件）， 部分类似于分治的思想（不懂得可以参考归并排序）， 通过求每一次的最优决策， 来得到一个最优解。在这里最重要的就是子问题的思想。

另一种理解方式数是DP的核心是加法原理（下文的人人为我形递归）和乘法原理（下文的我为人人形递归）， 通过这两个原理， 在当状态的前有限多个状态中找到最优解来求得当前状态， 而对于前一个或者前几个状态采用同样的方法知道求出边界状态，这种方法最恶心的就是边界状态


在学会搜索之后， 最简单入门DP的方法就是记忆话搜索， 但是后来会发现大多数DP题目因为时间和内存的限制并不能使用递归（函数的递归调用会占用栈内存， 另外函数的递归调用也将占用大量的时间）

* 子问题解决法的适用条件
需同时满足一下三点：

1.具有相同的子问题：我们必须保证我们分割成的子问题也能按照相同的方法分割成更小的自问题， 并这些自问题的最终分割情况是可以解决的。

2.满足最优子结构：就是一个决策的子决策也是最优的

3.无后效性：这是DP中最重要的一点， 他要求每个子问题的决策不能对后面其他未解决的问题产影响， 如果产生就无法保证决策的最优性， 这就是无后效性。往往需要我们找到一个合适的状态。


* 基本实现
1. 最优子结构：opt[n] = best_of(opt[n-1), ...)
1.1 递归的定义最优解（递推：递归 + 记忆化）
1.2 以自底向上或自顶向下的记忆方式计算出最优解
1.3 根据计算最优解时得到的信息构造问题的最优解
2. 定义状态：opt[n]（最关键步骤）
3. 状态转移方程
3.1 opt[i] = opt[n-1] + opt[n-2]
3.2 opt[i,j] = opt[i+1][j] + opt[i][j+1]（a[i,j] 是否为空）
```
# 状态定义
dp = ...

# 初始状态
dp[0][0] = i
dp[0][1] = j
...

# DP 状态的推导
for i in ...
    for j in ...
        d[i][j] = ...
        
# 最优解
return dp[m][n]
```
* 适用场景
1. 一个模型：多阶段决策最优解模型
2. 三个特征
2.1 最优子结构
2.2 无后效性
2.3 重复子问题
* 常考面试
1. 背包问题
2. 计算两个字符串的相似度
3. 最长公共子串长度
4. 求最长递增子序列
5. 最小编辑距离
6. 爬楼梯
7. 连续子数组的最大和
8. 最长回文子串
* 实战题目
1. [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)
2. [不同路径](https://leetcode-cn.com/problems/unique-paths/)
3. [不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/submissions/)
4. [不同路径 III](https://leetcode-cn.com/problems/unique-paths-iii/)
5. [零钱兑换](https://leetcode-cn.com/problems/coin-change/)
6. [零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/)
7. [三角形最小路径和](https://leetcode-cn.com/problems/triangle/)
8. [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
9. [编辑距离](https://leetcode-cn.com/problems/edit-distance/)
10. [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)
11. [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
12. [打家劫舍](https://leetcode-cn.com/problems/house-robber/)
13. [打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/description/)
14. [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
15. [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
16. [买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
17. [买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)
18. [最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
19. [买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)