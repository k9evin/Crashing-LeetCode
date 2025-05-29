/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    const str = s.toLowerCase();
    let left = 0;
    let right = str.length - 1;

    while (left < right) {
        // Skip non alpha or num characters
        while (left < right && !isAlphaNum(str[left])) {
            left++;
        }
        while (left < right && !isAlphaNum(str[right])) {
            right--;
        }
        // Check for equality
        if (str[left] !== str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
};

function isAlphaNum(c) {
    return (c >= 'A' && c <= 'Z' ||
        c >= 'a' && c <= 'z' ||
        c >= '0' && c <= '9');
};