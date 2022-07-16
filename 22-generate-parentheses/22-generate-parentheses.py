class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Solution 1:
        # Time complexity: O(2^n)  recursion function calls itself twice
        # Space complexity: O(n)
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            # valid solution if open == closed == n
            if openN == closedN == n:
                res.append("".join(stack))
            # only add open parenthesis if < n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # backtrack
                stack.pop()
            # only add closing parenthesis if < # of open parenthesis
            # you cannot have more closing parenthesis than the open one
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                # backtrack
                stack.pop()
        
        backtrack(0, 0)
        return res