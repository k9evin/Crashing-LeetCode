# Last updated: 2/2/2026, 6:21:22 PM
1class Container:
2    def __init__(self, k: int):
3        self.k = k
4        self.st1 = SortedList()
5        self.st2 = SortedList()
6        self.sm = 0
7
8    def adjust(self):
9        while len(self.st1) < self.k and len(self.st2) > 0:
10            x = self.st2[0]
11            self.st1.add(x)
12            self.st2.remove(x)
13            self.sm += x
14
15        while len(self.st1) > self.k:
16            x = self.st1[-1]
17            self.st2.add(x)
18            self.st1.remove(x)
19            self.sm -= x
20
21    # insert element x
22    def add(self, x: int):
23        if len(self.st2) > 0 and x >= self.st2[0]:
24            self.st2.add(x)
25        else:
26            self.st1.add(x)
27            self.sm += x
28        self.adjust()
29
30    # delete element x
31    def erase(self, x: int):
32        if x in self.st1:
33            self.st1.remove(x)
34            self.sm -= x
35        elif x in self.st2:
36            self.st2.remove(x)
37        self.adjust()
38
39    # sum of the first k smallest elements
40    def sum(self) -> int:
41        return self.sm
42
43
44class Solution:
45    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
46        n = len(nums)
47        cnt = Container(k - 2)
48        for i in range(1, k - 1):
49            cnt.add(nums[i])
50
51        ans = cnt.sum() + nums[k - 1]
52        for i in range(k, n):
53            j = i - dist - 1
54            if j > 0:
55                cnt.erase(nums[j])
56            cnt.add(nums[i - 1])
57            ans = min(ans, cnt.sum() + nums[i])
58
59        return ans + nums[0]