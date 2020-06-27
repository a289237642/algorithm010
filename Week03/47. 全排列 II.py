"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

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