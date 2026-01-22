# Last updated: 1/21/2026, 10:05:01 PM
1class Solution:
2    def validIPAddress(self, queryIP: str) -> str:
3        # 检查 IPv4：包含 '.'
4        if "." in queryIP:
5            parts = queryIP.split(".")
6
7            # IPv4 必须有 4 个部分
8            if len(parts) != 4:
9                return "Neither"
10
11            for part in parts:
12                # 验证每个部分：
13                # 1. 不能为空
14                # 2. 必须全是数字
15                # 3. 数值在 0-255 范围内
16                # 4. 不能有前导零（如 "01", "001"）
17                if (
18                    not part
19                    or not part.isdigit()
20                    or int(part) > 255
21                    or (len(part) > 1 and part[0] == "0")
22                ):
23                    return "Neither"
24            return "IPv4"
25
26        # 检查 IPv6：包含 ':'
27        elif ":" in queryIP:
28            parts = queryIP.split(":")
29
30            # IPv6 必须有 8 个部分
31            if len(parts) != 8:
32                return "Neither"
33
34            hex_chars = "0123456789abcdefABCDEF"  # 十六进制字符集
35            for part in parts:
36                # 验证每个部分：
37                # 1. 不能为空
38                # 2. 长度在 1-4 之间
39                # 3. 只能包含十六进制字符（0-9, a-f, A-F）
40                if not part or len(part) > 4 or not all(c in hex_chars for c in part):
41                    return "Neither"
42            return "IPv6"
43
44        # 既不包含 '.' 也不包含 ':'
45        else:
46            return "Neither"
47
48
49# Time Complexity: O(n)
50#   - n = len(queryIP)
51#   - split() 操作：O(n)
52#   - IPv4: 遍历 4 个部分，每部分最多 3 个字符，O(4×3) = O(1)
53#   - IPv6: 遍历 8 个部分，每部分最多 4 个字符，O(8×4) = O(32) = O(1)
54#   - 总体：O(n)，主要时间花在 split() 上
55
56# Space Complexity: O(1)
57