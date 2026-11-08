class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = (s1 + " " + s2).split()

        occurence = {}
        output = []
        for word in words:
            occurence[word] = occurence.get(word, 0) + 1
        for word in occurence:
            if occurence[word] == 1:
                output.append(word)
                
        return output