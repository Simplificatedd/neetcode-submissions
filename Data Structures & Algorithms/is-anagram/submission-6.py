class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        list1, list2 = list(s), list(t)
        return Counter(list1) == Counter(list2)