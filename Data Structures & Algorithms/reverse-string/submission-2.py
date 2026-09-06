class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s)/2
        start = 0
        end = len(s)-1
        while start < mid:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1