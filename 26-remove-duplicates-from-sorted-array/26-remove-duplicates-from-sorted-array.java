class Solution {
    public int removeDuplicates(int[] nums) {
        // Special case where the length of the array is 0
        if (nums.length == 0) return 0;
        
        // Use two pointers
        int slow = 0, fast = 0;
        
        while (fast < nums.length) {
            // If the value in the slow index is not the same
            // as the fast index, then assign the value in
            // the fast index to slow index++
            if (nums[slow] != nums[fast]) {
                slow++;
                nums[slow] = nums[fast];
            }
            
            // Increment fast index
            fast++;
        }
        
        // Return the length of the final array
        return slow + 1;
    }
}