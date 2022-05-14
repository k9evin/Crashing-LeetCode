class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) return 0;
        // Two pointer
        // int slow = 0, fast = 0;
        // while (fast < nums.length) {
        //     if (nums[fast] != val) {
        //         nums[slow++] = nums[fast];
        //     }
        //     fast++;
        // }
        // return slow;
        
        int i = 0;
        for (int n : nums)
            if (n != val)
                nums[i++] = n;
        return i;
    }
}