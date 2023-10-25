class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # base case
        if n == 1:
            return 0
            
        # if k is odd, then k is the same number as its parent
        if k % 2 != 0:
            return self.kthGrammar(n - 1, (k + 1) // 2)
        # if k is even, then k is the opposite number of its parent
        else:
            return 1 - self.kthGrammar(n - 1, (k + 1) // 2)

