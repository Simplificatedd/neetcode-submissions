class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in diction:
                return [diction[difference], i]

            diction[num] = i