"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https: // leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""





class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert(s):
            res = [0]*26
            for char in s:
                res[ord(char)-ord('a')] += 1
            return tuple(res)

        rec = {}
        res = []
        for s in strs:
            t = convert(s)

            if t in rec:
                res[rec[t]].append(s)
            else:
                res.append([s])
                rec[t] = len(res)-1
        return res
