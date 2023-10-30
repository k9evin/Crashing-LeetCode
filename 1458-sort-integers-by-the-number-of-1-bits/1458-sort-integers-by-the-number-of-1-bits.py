class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def hammingWeight(n: int) -> int:
            count = 0

            while n:
                # n & (n-1) will remove the rightmost 1 in binary representation of n
                n = n & (n - 1)
                count += 1
            
            return count
        
        arr.sort(key = lambda n: (hammingWeight(n), n))
        return arr