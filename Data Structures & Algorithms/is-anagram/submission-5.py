class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        list1 = list(s)
        list2 = list(t)
        return Counter(list1) == Counter(list2)