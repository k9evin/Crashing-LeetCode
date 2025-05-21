/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let sum = 0;
    let expectedSum = 0;

    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        expectedSum += i + 1;
    }

    return expectedSum - sum;
};