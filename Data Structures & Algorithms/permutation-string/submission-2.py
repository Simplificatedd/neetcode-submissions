class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original = {}

        for char in s1:
            original[char] = original.get(char, 0) + 1

        for i, char in enumerate(s2):
            if char in original:
                remaining = original.copy()
                for j in range(i, i + len(s1)):
                    if j >= len(s2):
                        break

                    current = s2[j]
                    if current not in remaining:
                        break

                    remaining[current] -= 1
                    if remaining[current] == 0:
                        del remaining[current]
                        
                if not remaining:
                    return True
        return False