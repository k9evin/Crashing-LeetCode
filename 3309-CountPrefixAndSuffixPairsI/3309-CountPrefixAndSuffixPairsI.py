# Last updated: 12/29/2025, 1:40:09 AM
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Counts the number of prefix-suffix pairs in the list of words.

        A word is considered a prefix-suffix pair if another word in the list starts
        and ends with the given word.

        Time Complexity: O(n^2 * m), where:
            - n is the number of words in the list.
            - m is the average length of the words (used for `startswith` and `endswith` checks).

        Space Complexity: O(1), as no extra data structures are used beyond simple variables.
        """
        res = 0

        # Iterate over all pairs of words
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word_i = words[i]  # Current word in the outer loop
                word_j = words[j]  # Current word in the inner loop

                # Check if word_j starts and ends with word_i
                if word_j.startswith(word_i) and word_j.endswith(word_i):
                    res += 1  # Increment the result if condition is met

        return res
