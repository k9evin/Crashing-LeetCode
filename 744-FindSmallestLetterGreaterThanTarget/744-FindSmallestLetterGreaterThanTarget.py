# Last updated: 2/1/2026, 4:56:58 PM
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        left = 0
4        right = len(letters) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8            if letters[mid] <= target:
9                left = mid + 1
10            else:
11                right = mid - 1
12
13        if left == len(letters):
14            return letters[0]
15        else:
16            return letters[left]
17