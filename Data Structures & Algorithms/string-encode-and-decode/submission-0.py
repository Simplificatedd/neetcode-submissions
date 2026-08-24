class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        init = 0
        while init < len(s):
            i = init

            while s[i] != '#':
                i += 1
            str_len = int(s[init:i])
            str_begin = i + 1
            str_end = str_begin + str_len

            decoded.append(s[str_begin:str_end])
            init = str_end
        return decoded