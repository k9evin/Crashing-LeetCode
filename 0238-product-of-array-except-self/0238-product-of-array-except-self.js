/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    // we will iterate through the nums array twice, the first forward iteration calculate the prefix product, the second backward iteration calculate the suffix product
    res = new Array(nums.length).fill(1);

    // example: nums = [1,2,3,4]
    // pref = [1,1,2,6]
    // ans = [1,1,2,6]
    let prefix = 1;
    for (let i = 0; i < nums.length; i++) {
        res[i] = prefix;
        prefix *= nums[i];
    }

    // suff = [24,12,4,1]
    // ans = [24,12,8,6]
    let postfix = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        res[i] *= postfix;
        postfix *= nums[i];
    }

    return res;
};