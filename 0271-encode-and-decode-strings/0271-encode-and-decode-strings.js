/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
var encode = function (strs) {
    let encodedStrs = "";

    for (let str of strs) {
        encodedStrs += str.length + "#" + str;
    }

    return encodedStrs;
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function (s) {
    let decodedStrs = [];
    let i = 0;

    while (i < s.length) {
        const delimIndex = s.indexOf("#", i);
        const strLength = parseInt(s.substring(i, delimIndex));
        const decodedStr = s.substring(delimIndex + 1, delimIndex + 1 + strLength);
        decodedStrs.push(decodedStr);
        i = delimIndex + 1 + strLength;
    }

    return decodedStrs;
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */