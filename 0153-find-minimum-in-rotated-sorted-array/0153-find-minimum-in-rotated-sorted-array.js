/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        let mid = left + Math.floor((right - left) / 2);
        // If nums[mid] > nums[right], the minimum is in the right half
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        }
        // If nums[mid] <= nums[right], the minimum is in the left half or nums[mid] itself
        else {
            right = mid;
        }
    }

    return nums[left];
};