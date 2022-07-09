class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
            print(result)
        return result

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        result = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i : j])
            result.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
