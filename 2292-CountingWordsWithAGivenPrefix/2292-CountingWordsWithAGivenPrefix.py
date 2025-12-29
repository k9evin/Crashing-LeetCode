# Last updated: 12/29/2025, 1:40:37 AM
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        This algorithm counts how many strings in the list `words` start with the given prefix `pref`:
        - Iterate through each word in the list.
        - Use the `startswith` method to check if the word begins with the prefix.
        - Increment the count if the prefix matches.

        Time Complexity: O(n * m), where n is the number of words and m is the length of the prefix.
        Space Complexity: O(1), as no extra space proportional to input size is used.
        """
        res = 0  # Initialize counter for matching words

        # Iterate through the list of words
        for w in words:
            # Check if the word starts with the given prefix
            if w.startswith(pref):
                res += 1  # Increment the counter if the condition is met

        return res  # Return the total count of matches
