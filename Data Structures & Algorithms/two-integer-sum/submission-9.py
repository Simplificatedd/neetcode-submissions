class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # num : index
        for i, num in enumerate(nums):
            difference = target - num
            if difference in dictionary.keys():
                return [dictionary.get(difference), i]
            dictionary[num] = i