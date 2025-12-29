// Last updated: 12/29/2025, 1:40:20 AM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
    const res = [];

    for (const i in arr) {
        res.push(fn(arr[i], Number(i)));
    }

    return res;
};