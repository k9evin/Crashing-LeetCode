class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1:
        # Time complexity: O(m * nlogn) 
        # m: number of words, n: length of words
        # Space complexity: O(mn)
        results = defaultdict(list)
        for word in strs:
            results["".join(sorted(word))].append(word)
        return list(results.values())
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
        
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()