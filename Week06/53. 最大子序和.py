"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 暴力求解---基本思路就是遍历一遍，用两个变量，一个记录最大的和，一个记录当前的和。时空复杂度貌似还不错......（时间复杂度 O(n)O(n)，空间复杂度 O(l)O(l)）


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1,n):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i]>nums[i]:
                max_ = max(max_, tmp+nums[i])
                tmp = tmp + nums[i]
            else:
            #当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
                max_ = max(max_, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_
        
# 分治法---分治法其他题解里将的很清楚了。其实就是它的最大子序和要么在左半边，要么在右半边，要么是穿过中间，对于左右边的序列，情况也是一样，因此可以用递归处理。中间部分的则可以直接计算出来，时间复杂度应该是 O(nlogn)O(nlogn)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #递归终止条件
        if n == 1:
            return nums[0]
        else:
            #递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            #递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        
        #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        #返回三个中的最大值
        return max(max_right,max_left,max_l+max_r)



