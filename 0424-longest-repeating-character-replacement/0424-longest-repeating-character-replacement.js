/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
    let count = new Map();
    let res = 0;
    let maxCharFreq = 0; // 优化点：维护当前窗口内最大字符频率

    let left = 0;
    for (let right = 0; right < s.length; right++) {
        // Update the frequency count
        count.set(s[right], (count.get(s[right]) || 0) + 1);

        // 优化：在每次添加字符时，更新maxCharFreq
        // 这样就不需要在while循环中每次都计算Math.max(...)
        maxCharFreq = Math.max(maxCharFreq, count.get(s[right]));

        // Remove the left most value if number of replacements exceed k
        // 这里的 (right - left + 1) 是当前窗口的长度
        // maxCharFreq 是当前窗口内出现频率最高的字符的数量
        // (right - left + 1) - maxCharFreq 就是需要替换的字符数量
        while ((right - left + 1) - maxCharFreq > k) {
            count.set(s[left], count.get(s[left]) - 1);
            // \U0001f41b 注意：当减小左侧字符的频率时，maxCharFreq 可能需要重新计算
            // 这是一个潜在的性能问题，但通常在滑动窗口问题中，这个while循环
            // 运行的次数是 O(N) 的，所以整体复杂度仍然是 O(N)。
            // 如果maxCharFreq减小，但它仍然是窗口中最大的，那没问题。
            // 如果它不再是最大的，我们需要找到新的最大值。
            // 实际上，对于这个特定的问题，我们不需要在`while`循环中重新计算`maxCharFreq`。
            // 原因是，我们只关心窗口的**最大可能长度**。
            // 当我们收缩窗口时（`left`移动），`maxCharFreq`可能不再是窗口的实际最大频率，
            // 但这不影响我们寻找最长子串的目标。
            // 只要 `maxCharFreq` 仍然保持**某个**字符的最大频率（即便它可能不是当前窗口中所有字符的最大频率），
            // 并且我们正在寻找最大可能的窗口长度，这种做法是有效的。
            // 解释：如果当前窗口的长度 `(right - left + 1)` 已经达到 `res` 的最大值，
            // 并且 `maxCharFreq` 是正确的，那么 `(right - left + 1) - maxCharFreq` 告诉我们是否需要收缩。
            // 当 `left` 移动时，窗口变小，`maxCharFreq` 可能会“过时”，
            // 但只要 `right - left + 1` 减去 `maxCharFreq` 仍然大于 `k`，
            // 就说明即使以当前的 `maxCharFreq` 来计算，我们仍然需要收缩窗口。
            // 这是一种被称为 "monotonic (非严格递减/递增)" 的优化，因为我们只关心窗口的最大长度。
            // 如果我们找到了一个有效长度 `L`，那么我们下一次的 `maxCharFreq`
            // 不会比 `L - k` 更小（如果 `L` 是最大长度），否则就无法维持这个长度。
            left += 1;
            // 这里的maxCharFreq不需要在while循环内部更新，因为即使当前的maxCharFreq
            // 变小了，我们仍然希望保持窗口尽可能大，
            // 而且只有当maxCharFreq代表的字符被移出窗口，并且它确实是唯一的最大频率时，
            // 这个问题才会变得更复杂。但在本题中，这种优化是有效的。
            // 更详细的解释在下面。
        }

        // Update result
        res = Math.max(res, right - left + 1);
    }

    return res;
};