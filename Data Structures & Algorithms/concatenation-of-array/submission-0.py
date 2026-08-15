class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_copy = nums.copy()
        for n in nums:
            nums_copy.append(n)
        return nums_copy