# Last updated: 2/11/2026, 6:16:30 PM
1class LazyTag:
2    def __init__(self):
3        self.to_add = 0
4
5    def add(self, other):
6        self.to_add += other.to_add
7        return self
8
9    def has_tag(self):
10        return self.to_add != 0
11
12    def clear(self):
13        self.to_add = 0
14
15
16class SegmentTreeNode:
17    def __init__(self):
18        self.min_value = 0
19        self.max_value = 0
20        self.lazy_tag = LazyTag()
21
22
23class SegmentTree:
24    def __init__(self, data):
25        self.n = len(data)
26        self.tree = [SegmentTreeNode() for _ in range(self.n * 4 + 1)]
27        self._build(data, 1, self.n, 1)
28
29    def add(self, l, r, val):
30        tag = LazyTag()
31        tag.to_add = val
32        self._update(l, r, tag, 1, self.n, 1)
33
34    def find_last(self, start, val):
35        if start > self.n:
36            return -1
37        return self._find(start, self.n, val, 1, self.n, 1)
38
39    def _apply_tag(self, i, tag):
40        self.tree[i].min_value += tag.to_add
41        self.tree[i].max_value += tag.to_add
42        self.tree[i].lazy_tag.add(tag)
43
44    def _pushdown(self, i):
45        if self.tree[i].lazy_tag.has_tag():
46            tag = LazyTag()
47            tag.to_add = self.tree[i].lazy_tag.to_add
48            self._apply_tag(i << 1, tag)
49            self._apply_tag((i << 1) | 1, tag)
50            self.tree[i].lazy_tag.clear()
51
52    def _pushup(self, i):
53        self.tree[i].min_value = min(
54            self.tree[i << 1].min_value, self.tree[(i << 1) | 1].min_value
55        )
56        self.tree[i].max_value = max(
57            self.tree[i << 1].max_value, self.tree[(i << 1) | 1].max_value
58        )
59
60    def _build(self, data, l, r, i):
61        if l == r:
62            self.tree[i].min_value = data[l - 1]
63            self.tree[i].max_value = data[l - 1]
64            return
65
66        mid = l + ((r - l) >> 1)
67        self._build(data, l, mid, i << 1)
68        self._build(data, mid + 1, r, (i << 1) | 1)
69        self._pushup(i)
70
71    def _update(self, target_l, target_r, tag, l, r, i):
72        if target_l <= l and r <= target_r:
73            self._apply_tag(i, tag)
74            return
75
76        self._pushdown(i)
77        mid = l + ((r - l) >> 1)
78        if target_l <= mid:
79            self._update(target_l, target_r, tag, l, mid, i << 1)
80        if target_r > mid:
81            self._update(target_l, target_r, tag, mid + 1, r, (i << 1) | 1)
82        self._pushup(i)
83
84    def _find(self, target_l, target_r, val, l, r, i):
85        if self.tree[i].min_value > val or self.tree[i].max_value < val:
86            return -1
87
88        if l == r:
89            return l
90
91        self._pushdown(i)
92        mid = l + ((r - l) >> 1)
93
94        if target_r >= mid + 1:
95            res = self._find(target_l, target_r, val, mid + 1, r, (i << 1) | 1)
96            if res != -1:
97                return res
98
99        if l <= target_r and mid >= target_l:
100            return self._find(target_l, target_r, val, l, mid, i << 1)
101
102        return -1
103
104
105class Solution:
106    def longestBalanced(self, nums: List[int]) -> int:
107        occurrences = defaultdict(deque)
108
109        def sgn(x):
110            return 1 if x % 2 == 0 else -1
111
112        length = 0
113        prefix_sum = [0] * len(nums)
114        prefix_sum[0] = sgn(nums[0])
115        occurrences[nums[0]].append(1)
116
117        for i in range(1, len(nums)):
118            prefix_sum[i] = prefix_sum[i - 1]
119            occ = occurrences[nums[i]]
120            if not occ:
121                prefix_sum[i] += sgn(nums[i])
122            occ.append(i + 1)
123
124        seg = SegmentTree(prefix_sum)
125        for i in range(len(nums)):
126            length = max(length, seg.find_last(i + length, 0) - i)
127            next_pos = len(nums) + 1
128            occurrences[nums[i]].popleft()
129            if occurrences[nums[i]]:
130                next_pos = occurrences[nums[i]][0]
131
132            seg.add(i + 1, next_pos - 1, -sgn(nums[i]))
133
134        return length
135