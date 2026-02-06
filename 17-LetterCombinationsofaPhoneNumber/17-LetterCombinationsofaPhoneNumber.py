# Last updated: 2/5/2026, 7:50:43 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        mapping = {
4            "2": "abc",
5            "3": "def",
6            "4": "ghi",
7            "5": "jkl",
8            "6": "mno",
9            "7": "pqrs",
10            "8": "tuv",
11            "9": "wxyz",
12        }
13
14        res = []
15
16        def backtrack(i, path):
17            if i == len(digits):
18                res.append("".join(path))
19                return
20
21            possible_letters = mapping.get(digits[i], "")
22
23            for letter in possible_letters:
24                path.append(letter)
25                backtrack(i + 1, path)
26                path.pop()
27
28        backtrack(0, [])
29
30        return res
31