class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # 由中间向两边扩散
        for i in range(len(s)):
            # 奇数长度
            l, r = i, i
            # 确保l, r在范围内，而且这两个字符串相同才算palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 字符串长度比现在res长，才更新res
                if (r - l + 1) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
            # 偶数长度
            l, r = i, i + 1
            # 确保l, r在范围内，而且这两个字符串相同才算palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 字符串长度比现在res长，才更新res
                if (r - l + 1) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
        return res
