# Last updated: 12/29/2025, 1:40:29 AM
class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Count the frequency of each character
        char_counter = collections.Counter(word)

        # For each character in the word, try to remove it
        for c in word:
            char_counter[c] -= 1
            # If the frequency becomes 0, we don't have this char anymore
            if char_counter[c] == 0:
                char_counter.pop(c)
            # Return true if every chars' frequency are the same
            if len(set(char_counter.values())) == 1:
                return True
            # Add the character back
            char_counter[c] += 1

        return False
