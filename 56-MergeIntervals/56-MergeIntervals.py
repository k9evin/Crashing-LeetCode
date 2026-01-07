# Last updated: 1/6/2026, 11:13:21 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        """
4        Merges overlapping intervals from a given list of intervals.
5
6        Algorithm:
7        - Sort the intervals by their starting times.
8        - Use a single pass to iterate through the sorted intervals:
9          - If the current interval overlaps with the last interval in the merged list,
10            update the end of the last interval to be the maximum of the two.
11          - Otherwise, append the current interval to the merged list.
12        - Return the merged list.
13
14        Time Complexity:
15        - O(n log n) for sorting the intervals (where n is the number of intervals).
16        - O(n) for the single pass to merge intervals.
17        - Overall: O(n log n).
18
19        Space Complexity:
20        - O(n) for the output list `merged`.
21        - If sorting in-place, no additional space for sorting.
22
23        """
24        if not intervals:  # Handle empty input
25            return []
26
27        intervals.sort()  # Sort by start time (default behavior)
28
29        merged = [intervals[0]]
30        for interval in intervals[1:]:
31            # Overlapping: current start <= last end
32            if interval[0] <= merged[-1][1]:
33                merged[-1][1] = max(merged[-1][1], interval[1])  # Extend end
34            else:
35                merged.append(interval)  # No overlap, add new interval
36
37        return merged
38