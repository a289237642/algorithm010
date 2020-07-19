"""

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

 

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

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