/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const charCounts = new Map();

    for (let i = 0; i < s.length; i++) {
        const charS = s[i];
        const charT = t[i];

        charCounts.set(charS, (charCounts.get(charS) || 0) + 1);
        charCounts.set(charT, (charCounts.get(charT) || 0) - 1);
    }

    for (let count of charCounts.values()) {
        if (count !== 0) {
            return false;
        }
    }

    return true;
};