"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
                1
             1     1
        1    2     2     1  
        



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        p = [1]
        if not rowIndex:
            return p
        for j in range(rowIndex):
            p= [1] + [p[i]+p[i+1] for i in range(len(p)-1)]+[1]
        return p