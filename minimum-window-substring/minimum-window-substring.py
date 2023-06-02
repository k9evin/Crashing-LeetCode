class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        left, right = 0, 1
        res = ''
        length = float("infinity")
        satisfied = 0

        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1

        for right in range(len(s)):
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
                if t_dict[s[right]] == 0:
                    satisfied += 1
            while satisfied == len(t_dict):
                if (right - left + 1) < length:
                    res = s[left: right + 1]
                    length = len(res)
                if s[left] in t_dict:
                    if t_dict[s[left]] == 0:
                        satisfied -= 1
                    t_dict[s[left]] += 1
                left += 1
        return res
                
