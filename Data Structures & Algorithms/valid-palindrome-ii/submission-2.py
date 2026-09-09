class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                output = (checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1) )
                return output
            left += 1
            right -= 1
        return True