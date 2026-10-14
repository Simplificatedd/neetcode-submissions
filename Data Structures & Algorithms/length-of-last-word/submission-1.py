class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        word = False
        if len(s) == 1:
            if s[0] == " ":
                return 0
            else:
                return 1
        for i in range(len(s) - 1, 0, -1):
            if s[i] == " " and word:
                return length
            if s[i] != " ":
                length += 1
            if length > 1:
                word = True
        return length