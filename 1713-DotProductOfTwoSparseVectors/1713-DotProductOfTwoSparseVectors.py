# Last updated: 12/29/2025, 1:41:22 AM
class SparseVector:
    def __init__(self, nums: List[int]):
        # create an index-value pairs excluding 0
        self.pairs = [(i, v) for i, v in enumerate(nums) if v != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1, p2 = 0, 0
        res = 0

        while p1 < len(self.pairs) and p2 < len(vec.pairs):
            # if both pairs have the same index, multiply them
            if self.pairs[p1][0] == vec.pairs[p2][0]:
                res += self.pairs[p1][1] * vec.pairs[p2][1]
                p1 += 1
                p2 += 1
            elif self.pairs[p1][0] > vec.pairs[p2][0]:
                p2 += 1
            else:
                p1 += 1
        
        return res

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)