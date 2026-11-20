class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s = list(s)
        t = list(t)
        index_t = 0
        for i, char in enumerate(s):
            print(index_t)
            if index_t < len(t) and t[index_t] == char:
                index_t += 1
        return len(t) - index_t
