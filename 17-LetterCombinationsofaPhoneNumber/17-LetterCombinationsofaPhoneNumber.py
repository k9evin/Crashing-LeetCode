# Last updated: 2/5/2026, 7:54:20 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        # 数字到字母的映射表
4        mapping = {
5            "2": "abc",
6            "3": "def",
7            "4": "ghi",
8            "5": "jkl",
9            "6": "mno",
10            "7": "pqrs",  # 7和9有4个字母
11            "8": "tuv",
12            "9": "wxyz",
13        }
14
15        res = []  # 存储所有可能的组合
16
17        # 回溯函数：i表示当前处理的数字索引，path存储当前路径
18        def backtrack(i, path):
19            # 终止条件：处理完所有数字
20            if i == len(digits):
21                res.append("".join(path))  # 将路径转换为字符串
22                return
23
24            # 获取当前数字对应的所有字母
25            possible_letters = mapping.get(digits[i], "")
26
27            # 遍历当前数字的每个可能字母
28            for letter in possible_letters:
29                path.append(letter)  # 选择当前字母
30                backtrack(i + 1, path)  # 递归处理下一个数字
31                path.pop()  # 撤销选择，回溯
32
33        # 只有当有输入数字时才进行回溯
34        backtrack(0, [])
35
36        return res
37
38
39# 时间复杂度：O(4^n)，每个数字最多对应4个字母（7和9），n为数字长度
40# 空间复杂度：O(n)，递归调用栈深度和path长度最多为n
41