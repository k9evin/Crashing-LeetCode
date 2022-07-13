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
        str_length = float("infinity")
        
        for r in range(len(s)):
            if s[r] in t_count:
                t_count[s[r]] -= 1
                if t_count[s[r]] == 0:
                    matches += 1
            while matches == len(t_count):
                if (r - l + 1) < str_length:
                    start, end = l, r
                    ans = s[start: end + 1]
                    str_length = r - l + 1
                    print(ans)
                if s[l] in t_count:
                    if t_count[s[l]] == 0:
                        matches -= 1
                    t_count[s[l]] += 1
                l += 1
        return ans