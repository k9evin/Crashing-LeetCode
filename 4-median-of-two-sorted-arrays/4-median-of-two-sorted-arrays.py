class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Solution 1:
        # Time complexity: O(log(min(m,n)))
        # Space complexity: O(1)
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2
        
        # we need to make sure the first array is
        # always the shortest
        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) - 1
        
        while True:
            aMid = (l + r) // 2
            bMid = half - aMid - 2  # we want the index
            
            aLeft = a[aMid] if aMid >= 0 else float("-inf")
            bLeft = b[bMid] if bMid >= 0 else float("-inf")
            # we need to take care of out of bound situation
            aRight = a[aMid + 1] if (aMid + 1) < len(a) else float("inf")
            bRight = b[bMid + 1] if (bMid + 1) < len(b) else float("inf")
            
            # the partition is valid
            if aLeft <= bRight and bLeft <= aRight:
                # check if the length is odd
                if total % 2 != 0:
                    return min(aRight, bRight)
                # even
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            # reduce the A partition
            elif aLeft > bLeft:
                r = aMid - 1
            else:
                l = aMid + 1
                    
            
            
        