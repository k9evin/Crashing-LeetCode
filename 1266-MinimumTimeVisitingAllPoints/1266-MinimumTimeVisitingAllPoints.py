# Last updated: 1/11/2026, 11:45:35 PM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        min_time = 0
        
        # Traverse each consecutive pair of points
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            
            # Calculate the minimum time between two points
            # Since we can move diagonally, the time is determined by
            # the larger of horizontal and vertical distances
            # Example: (0,0) -> (3,4) takes max(3,4) = 4 seconds
            # Path: diagonal 3 steps + vertical 1 step = 4 total
            min_time += max(abs(target_x - curr_x), abs(target_y - curr_y))
        
        return min_time
        
        # Time Complexity: O(n)
        # - n is the number of points
        # - We iterate through all consecutive pairs exactly once
        
        # Space Complexity: O(1)
        # - Only using constant extra space for variables
        # - No additional data structures needed