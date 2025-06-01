/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
    `
    Finds all unique triplets in a list of integers that sum to zero

    Time Complexity: O(n^2), where n is the length of the input list
    Space Complexity: O(1) if sorting is done in-place
    `
    let res = [];
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        // If current num is positive, remaining values cannot sum to zero
        if (nums[i] > 0) {
            break;
        }
        // Skip dulplicates
        if (i === 0 || nums[i] !== nums[i - 1]) {
            // TwoSum two pointers
            let l = i + 1, r = nums.length - 1;
            while (l < r) {
                total = nums[i] + nums[l] + nums[r];
                if (total > 0) {
                    r--;
                } else if (total < 0) {
                    l++;
                } else {
                    res.push([nums[i], nums[l], nums[r]]);
                    l++, r--;
                    // Increment left while the next value is the same as the previous one
                    while (l < r && nums[l] === nums[l - 1]) {
                        l++;
                    }
                }
            }
        }
    }
    return res;
};