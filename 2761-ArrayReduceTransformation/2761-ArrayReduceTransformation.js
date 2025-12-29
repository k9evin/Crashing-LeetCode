// Last updated: 12/29/2025, 1:40:18 AM
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {
    let accum = init;

    nums.forEach((num) => {
        accum = fn(accum, num);
    })

    return accum;
};