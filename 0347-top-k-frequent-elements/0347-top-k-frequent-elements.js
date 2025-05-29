/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    // Bucket sort
    const count = {};
    const bucket = Array.from({ length: nums.length + 1 }, () => []);

    for (const num of nums) {
        count[num] = (count[num] || 0) + 1;
    }
    
    for (const key in count) {
        const freq = count[key];
        bucket[freq].push(parseInt(key));
    }

    const res = [];
    for (let i = bucket.length - 1; i >= 0; i--) {
        for (const num of bucket[i]) {
            res.push(num);
            if (res.length == k) {
                return res;
            }
        }
    }

};