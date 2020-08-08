"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 

提示：你可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import OrderedDict


class Solution(object):

    def firstUniqChar(self, s: str) -> int:
        odict = OrderedDict()

        # 记录字符出现次数
        for c in s:
            odict[c] = odict[c] + 1 if c in odict else 1

        # 利用有序的特性，在字典中找出首个出现次数为一的字符串
        for k, v in odict.items():
            if v == 1:
                # 返回字符串首次出现的位置
                return s.index(k)

        return -1


