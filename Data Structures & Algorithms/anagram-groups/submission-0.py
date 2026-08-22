class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for string in strs:
            index = [0] * 26 # 26 characters in alphabet
            for char in string:
                index[ord(char) - ord('a')] += 1
            output[tuple(index)].append(string)
        return list(output.values())