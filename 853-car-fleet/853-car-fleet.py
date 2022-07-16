class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        stack = []
        
        for p, s in sorted(zip(position, speed))[::-1]:
            # the remaining distance
            dist = target - p
            # if the stack is empty, append the required time to the stack
            if not stack:
                stack.append((dist / s))
            # if the time is larger than the time in the stack,
            # which means it won't catch up with the prev car
            # by the time passes the destination
            elif (dist / s) > stack[-1]:
                stack.append((dist / s))
        # the length of the stack represents the number of car fleets
        return len(stack)
            