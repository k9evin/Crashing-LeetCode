/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
    let count = new Map();
    let res = 0;

    let left = 0;
    for (let right = 0; right < s.length; right++) {
        // Update the frequency count
        count.set(s[right], (count.get(s[right]) || 0) + 1);

        // Remove the left most value if number of replacements exceed k
        // NOTE: count.values() returns an iterator, we need to spread it to an array
        while (((right - left + 1) - Math.max(...count.values())) > k) {
            count.set(s[left], count.get(s[left]) - 1);
            left += 1;
        }

        // Update result
        res = Math.max(res, right - left + 1);
    }

    return res;
};