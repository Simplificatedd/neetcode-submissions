class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        if len(str1) > len(str2):
            return False
        if str1 == str2:
            return True
        if str1 != str2[0:len(str1)]:
            return False
        if str1 != str2[len(str2)-len(str1):len(str2)]:
            return False
        
        return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        if len(words) < 2:
            return 0
        count = 0
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if j <= i:
                    continue
                if self.isPrefixAndSuffix(word1, word2):
                    count += 1

        return count
        