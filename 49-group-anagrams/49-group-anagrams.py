class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n: number of words, m: length of words
        
        # Solution 1:
        # Time complexity: O(n*mlogm) 
        # Space complexity: O(nm)
        # results = defaultdict(list)
        # for word in strs:
        #     results["".join(sorted(word))].append(word)
        # return list(results.values())
		
		# Solution 2:
        # Time complexity: O(nm)
        # Space complexity: O(n)
        results = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            results[tuple(freq)].append(word)
        return list(results.values())