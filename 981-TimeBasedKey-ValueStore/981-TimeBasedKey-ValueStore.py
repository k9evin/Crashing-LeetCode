# Last updated: 1/1/2026, 11:34:06 PM
1class TimeMap:
2
3    def __init__(self):
4        self.store = {}  # {key: [[val, timestamp], [val, timestamp]]}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.store:
8            self.store[key] = []
9        self.store[key].append([value, timestamp])
10
11    def get(self, key: str, timestamp: int) -> str:
12        values = self.store.get(key, [])
13        if not values:
14            return ""
15
16        l, r = 0, len(values) - 1
17        res = ""
18        while l <= r:
19            m = l + (r - l) // 2
20            if values[m][1] == timestamp:
21                return values[m][0]
22            elif values[m][1] < timestamp:
23                res = values[m][0]
24                l = m + 1
25            else:
26                r = m - 1
27
28        return res
29
30
31# Your TimeMap object will be instantiated and called as such:
32# obj = TimeMap()
33# obj.set(key,value,timestamp)
34# param_2 = obj.get(key,timestamp)
35