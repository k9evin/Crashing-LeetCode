class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        l, r = 0, 0
        t_count = Counter(t)
        matches = 0
        start, end = 0, 0
        ans = ""
        ans_length = float("infinity")
        
        for r in range(len(s)):
            # 向右扩展窗口直到包含所有 t 中的字符
            # 如果字符在 t_count 中，就递减字符 frequency
            if s[r] in t_count:
                t_count[s[r]] -= 1
                # 如果字符 frequency 为 0，代表该字符已符合
                if t_count[s[r]] == 0:
                    matches += 1
            # 只要 matches 符合要求，缩短左边窗口
            while matches == len(t_count):
                # 新字符串长度比 ans 长度短时才更新 ans
                if (r - l + 1) < ans_length:
                    start, end = l, r
                    ans = s[start: end + 1]
                    ans_length = r - l + 1
                # 当移除最左边的字符时该字符为 t 中的字符
                # 减少 matches
                if s[l] in t_count:
                    if t_count[s[l]] == 0:
                        matches -= 1
                    t_count[s[l]] += 1
                # left 指针递增
                l += 1
        return ans
    
        # Solution 2:
        # Time complexity: O(n)
        # Space complexity: O(1)
#         if t == "": return ""

#             countT, window = {}, {}
#             for c in t:
#                 countT[c] = 1 + countT.get(c, 0)

#             have, need = 0, len(countT)
#             res, resLen = [-1, -1], float("infinity")
#             l = 0
#             for r in range(len(s)):
#                 c = s[r]
#                 window[c] = 1 + window.get(c, 0)

#                 if c in countT and window[c] == countT[c]:
#                     have += 1

#                 while have == need:
#                     # update our result
#                     if (r - l + 1) < resLen:
#                         res = [l, r]
#                         resLen = (r - l + 1)
#                     # pop from the left of our window
#                     window[s[l]] -= 1
#                     if s[l] in countT and window[s[l]] < countT[s[l]]:
#                         have -= 1
#                     l += 1
#             l, r = res
#             return s[l:r+1] if resLen != float("infinity") else ""