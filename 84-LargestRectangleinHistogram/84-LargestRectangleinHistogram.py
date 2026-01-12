# Last updated: 1/11/2026, 11:13:01 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add sentinel values (0) at both ends to handle edge cases
        # This ensures all bars will eventually be popped from stack
        heights = [0] + heights + [0]
        max_area = 0
        stack = [0]  # Stack stores indices of bars in increasing height order
        
        for i in range(1, len(heights)):
            # Pop bars from stack when current bar is shorter
            # Each popped bar can be the shortest in a rectangle
            while heights[i] < heights[stack[-1]]:
                # Get the index of the bar to calculate area for
                center_idx = stack.pop()
                height = heights[center_idx]
                
                # Left boundary: the bar after the new top of stack
                # Right boundary: current position (exclusive)
                left_boundary = stack[-1]
                right_boundary = i
                width = right_boundary - left_boundary - 1
                
                # Update maximum area found
                max_area = max(max_area, height * width)
            
            # Push current index to stack
            stack.append(i)
        
        return max_area
        
        # Time Complexity: O(n)
        # - Each element is pushed and popped from stack at most once
        # - Total operations are linear with respect to input size
        
        # Space Complexity: O(n)
        # - Stack stores at most n indices in the worst case
        # - Modified heights array also takes O(n) space