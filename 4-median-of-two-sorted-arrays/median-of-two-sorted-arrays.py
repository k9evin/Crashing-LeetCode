class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        merged = []

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        while p1 < m:
            merged.append(nums1[p1])
            p1 += 1
        while p2 < n:
            merged.append(nums2[p2])
            p2 += 1

        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
        else:
            return merged[len(merged) // 2]
