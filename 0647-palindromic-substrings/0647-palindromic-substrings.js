/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
    function countPalindrome(left, right) {
        let count = 0;
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            count++;
            left--;
            right++;
        }
        return count;
    }

    let res = 0;
    for (let i = 0; i < s.length; i++) {
        res += countPalindrome(i, i);
        res += countPalindrome(i, i + 1);
    }
    return res;
};