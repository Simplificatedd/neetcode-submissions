class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        negative = 0
        for num in nums:
            if num < 0:
                negative += 1
        return 1 if negative % 2 == 0 else -1