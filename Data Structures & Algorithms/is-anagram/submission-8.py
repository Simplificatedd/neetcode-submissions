class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = sorted(list(s))
        tlist = sorted(list(t))
        return slist == tlist