# Last updated: 1/1/2026, 11:34:47 PM
1class TimeMap:
2
3    def __init__(self):
4        self.store = {}  # {key: [[val, timestamp], [val, timestamp]]}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        # O(1) amortized - append to list for given key
8        if key not in self.store:
9            self.store[key] = []
10        self.store[key].append([value, timestamp])
11
12    def get(self, key: str, timestamp: int) -> str:
13        # O(log n) - binary search where n = number of entries for key
14        values = self.store.get(key, [])
15        if not values:
16            return ""
17
18        l, r = 0, len(values) - 1
19        res = ""  # Track most recent valid value (timestamp <= target)
20
21        while l <= r:
22            m = (l + r) // 2
23            if values[m][1] <= timestamp:
24                res = values[m][0]  # Valid candidate found
25                l = m + 1  # Search right half for more recent valid entry
26            else:
27                r = m - 1  # Current timestamp too large, search left half
28
29        return res
30