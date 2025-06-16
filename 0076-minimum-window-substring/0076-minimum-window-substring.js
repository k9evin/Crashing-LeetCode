/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
    if (t.length > s.length) {
        return '';
    }

    // Count the frequency of the t string
    let countT = {};
    for (let c of t) {
        countT[c] = (countT[c] || 0) + 1;
    }

    // Character frequency in the current window
    let window = {};
    let satisfied = 0;
    let need = Object.keys(countT).length;
    let minLen = Infinity;
    let minSub = [-1, -1];

    // Sliding window
    let l = 0;
    for (let r = 0; r < s.length; r++) {
        // Include the new character
        let c = s[r];
        window[c] = (window[c] || 0) + 1;
        // Increment the count, if we have satisfied a character
        if (countT[c] && window[c] === countT[c]) {
            satisfied++;
        }

        // Update the minLen and minSub if we satisfy all the need
        while (satisfied === need) {
            if ((r - l + 1) < minLen) {
                minLen = r - l + 1;
                minSub = [l, r];
            }
            // Shrink the left side and continue searching
            window[s[l]]--;
            // If the removed left character is in the need, update count if necessary
            if (countT[s[l]] && window[s[l]] < countT[s[l]]) {
                satisfied--;
            }
            l++;
        }
    }

    return minLen === Infinity ? "" : s.slice(minSub[0], minSub[1] + 1);
};