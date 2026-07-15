class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Read the length
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1

            length = int(length)

            # Skip the '#'
            i += 1

            # Read the word
            word = s[i:i + length]
            res.append(word)

            # Move to the next encoded string
            i += length

        return res