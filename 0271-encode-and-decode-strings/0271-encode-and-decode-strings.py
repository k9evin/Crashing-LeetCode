class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_strs = ""

        for s in strs:
            encoded_strs += str(len(s)) + "|" + s

        return encoded_strs

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0

        while i < len(s):
            delim = s.find("|", i)
            length = int(s[i: delim])
            decoded_strs.append(s[delim + 1: delim + 1 + length])
            i = delim + 1 + length

        return decoded_strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
