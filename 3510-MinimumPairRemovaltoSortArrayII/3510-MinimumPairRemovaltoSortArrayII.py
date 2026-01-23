# Last updated: 1/23/2026, 6:36:52 PM
1class Node:
2    def __init__(self, value, left):
3        self.value = value
4        self.left = left
5        self.prev = None
6        self.next = None
7
8
9class Solution:
10    def minimumPairRemoval(self, nums: List[int]) -> int:
11        class PQItem:
12            def __init__(self, first, second, cost):
13                self.first = first
14                self.second = second
15                self.cost = cost
16
17            def __lt__(self, other):
18                if self.cost == other.cost:
19                    return self.first.left < other.first.left
20                return self.cost < other.cost
21
22        pq = []
23        head = Node(nums[0], 0)
24        current = head
25        merged = [False] * len(nums)
26        decrease_count = 0
27        count = 0
28
29        for i in range(1, len(nums)):
30            new_node = Node(nums[i], i)
31            current.next = new_node
32            new_node.prev = current
33            heapq.heappush(
34                pq, PQItem(current, new_node, current.value + new_node.value)
35            )
36
37            if nums[i - 1] > nums[i]:
38                decrease_count += 1
39
40            current = new_node
41
42        while decrease_count > 0:
43            item = heapq.heappop(pq)
44            first, second, cost = item.first, item.second, item.cost
45
46            if (
47                merged[first.left]
48                or merged[second.left]
49                or first.value + second.value != cost
50            ):
51                continue
52            count += 1
53
54            if first.value > second.value:
55                decrease_count -= 1
56
57            prev_node = first.prev
58            next_node = second.next
59            first.next = next_node
60            if next_node:
61                next_node.prev = first
62
63            if prev_node:
64                if prev_node.value > first.value and prev_node.value <= cost:
65                    decrease_count -= 1
66                elif prev_node.value <= first.value and prev_node.value > cost:
67                    decrease_count += 1
68
69                heapq.heappush(
70                    pq, PQItem(prev_node, first, prev_node.value + cost)
71                )
72
73            if next_node:
74                if second.value > next_node.value and cost <= next_node.value:
75                    decrease_count -= 1
76                elif second.value <= next_node.value and cost > next_node.value:
77                    decrease_count += 1
78                heapq.heappush(
79                    pq, PQItem(first, next_node, cost + next_node.value)
80                )
81
82            first.value = cost
83            merged[second.left] = True
84
85        return count