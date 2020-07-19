"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         f = [[0] * n for _ in range(n)]
#         f[0][0] = triangle[0][0]

#         for i in range(1, n):
#             f[i][0] = f[i - 1][0] + triangle[i][0]
#             for j in range(1, i):
#                 f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
#             f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        
#         return min(f[n - 1])

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle)-2, -1 ,-1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]