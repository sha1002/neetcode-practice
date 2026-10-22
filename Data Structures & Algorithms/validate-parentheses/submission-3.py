class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        apple = []
        for i in range(len(s)):
            if s[i] == '('or s[i] == '['or s[i] == '{':
                apple.append(s[i])
            else:
                if not apple:
                    return False
                top=apple.pop()
                if s[i] == ')'and top != '(':
                    return False
                if s[i] == ']'and top != '[':
                    return False
                if s[i] == '}'and top != '{':
                    return False
        return len(apple) == 0