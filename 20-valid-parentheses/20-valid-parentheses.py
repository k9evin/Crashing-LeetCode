class Solution:
    def isValid(self, s: str) -> bool:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        stack = []
        # every closed bracket has a correspond open bracket
        hashmap = {")" : "(", "]" : "[", "}" : "{"}
        
        for char in s:
            # if the character is in the hashmap, which means
            # it should have a correspond open bracket
            if char in hashmap:
                # if we found a open bracket, we should pop it
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                # otherwise, the bracket is not closed in the
                # correct order
                else:
                    return False
            # if it was a open bracket, append it to the stack
            else:
                stack.append(char)
        # return true if the stack is empty, false otherwise
        return True if not stack else False