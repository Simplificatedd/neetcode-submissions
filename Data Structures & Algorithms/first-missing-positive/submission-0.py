class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        missing = 1

        while missing in seen:
            missing += 1

        return missing