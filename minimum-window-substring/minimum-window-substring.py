class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        left, right = 0, 1
        res = ''
        length = float("infinity")

        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1

        for right in range(len(s)):
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
            while all(val <= 0 for val in t_dict.values()):
                if (right - left + 1) < length:
                    res = s[left: right + 1]
                    length = len(res)
                if s[left] in t_dict:
                    t_dict[s[left]] += 1
                left += 1
            #     print('in while loop')
            # print(t_dict, res, len(res), length, s[left:right+1])
        return res
                
