class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""

        for char in s:
            if char.isalnum():
                clean_char = char.lower()
                
                clean_str += clean_char

        return clean_str == clean_str[::-1]
