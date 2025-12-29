# Last updated: 12/29/2025, 1:40:11 AM
class Solution:
    def sortVowels(self, s: str) -> str:
        sorted_vowels = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)
        return ''.join([sorted_vowels.pop() if c.lower() in 'aeiou' else c for c in s])