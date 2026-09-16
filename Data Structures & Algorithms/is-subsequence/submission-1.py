class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_index = 0
        s_index_end = len(s) - 1
        for char in t:
            if s[s_index] == char:
                if s_index == s_index_end:
                    return True
                s_index += 1
        return False