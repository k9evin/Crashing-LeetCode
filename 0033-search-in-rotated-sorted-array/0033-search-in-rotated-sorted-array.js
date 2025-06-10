/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);

        // Case 1: find the target
        if (nums[mid] === target) {
            return mid;
        }
        // Case 2: the left portion of the array is sorted
        if (nums[left] <= nums[mid]) {
            // Target is in the left portion, shrink right side
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1;
            } 
            // Target is in the right portion, shrink left side
            else {
                left = mid + 1;
            }
        }
        // Case 3: the right portion of the array is sorted 
        else {
            // Target is in the right portion, shrink left side
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1;
            } 
            // Target is in the left portion, shrink right side
            else {
                right = mid - 1;
            }
        }
    }

    return -1;
};