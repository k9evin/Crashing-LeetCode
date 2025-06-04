/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const stack = [];
    const bracketPairs = { ')': '(', '}': '{', ']': '[' };

    for (const c of s) {
        // If we have a closing bracket
        if (bracketPairs[c]) {
            // If the stack is not empty and the last element matches the closing bracket, then we have a pair
            if (stack.length > 0 && stack[stack.length - 1] === bracketPairs[c]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            // If we have an opening bracket, append it to the stack
            stack.push(c);
        }
    }

    // Stack should be empty if all valid
    return stack.length === 0;
};