class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        stack = []
        maxArea = 0
        
        for i, h in enumerate(heights):
            # the start index represents the furthest index the
            # current element can extend to the left
            start = i
            # if the top element in the stack is heigher than the
            # current element, pop from the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (height * (i - index)))
                start = index
            # append a pair of value
            stack.append((start, h))
        
        # calculate the area from the remaining element in the stack
        for i, h in stack:
            maxArea = max(maxArea, (h * (len(heights) - i)))
        
        return maxArea