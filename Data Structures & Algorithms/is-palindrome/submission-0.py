class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                cleaned += char
        copy_of_s = list(cleaned)
        copy_of_s.reverse()
        return copy_of_s == list(cleaned)