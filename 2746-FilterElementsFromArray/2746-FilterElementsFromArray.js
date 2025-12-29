// Last updated: 12/29/2025, 1:40:21 AM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
    const filteredArr = [];

    for (const i in arr) {
        if (fn(arr[i], Number(i))) {
            filteredArr.push(arr[i]);
        }
    }

    return filteredArr;
};