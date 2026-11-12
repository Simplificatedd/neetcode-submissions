class Solution:
    def isPrefix(self, pref: str, word: str) -> bool:
        for i in range(len(pref)):
            if pref[i] != word[i]:
                return False
        return True

    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if self.isPrefix(pref, word):
                count += 1
        return count