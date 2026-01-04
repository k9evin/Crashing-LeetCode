# Last updated: 1/4/2026, 6:26:24 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        # Start with a carry of 1 (since we're adding one)
4        carry = 1
5
6        # Traverse the digits from right to left (least to most significant)
7        for i in range(len(digits) - 1, -1, -1):
8            # Add the current digit and the carry
9            temp_sum = digits[i] + carry
10            # The new digit is the remainder when divided by 10
11            new_digit = temp_sum % 10
12            digits[i] = new_digit
13            # Update carry for the next iteration (1 if overflow, else 0)
14            carry = temp_sum // 10
15
16        # If there's still a carry after processing all digits, prepend 1
17        if carry:
18            digits = [1] + digits
19
20        return digits
21
22
23# Time Complexity: O(n) — we iterate through the digits once.
24# Space Complexity: O(1) auxiliary space — we modify the input list in place.
25