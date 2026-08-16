class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {} # {value : index}
        for i, num in enumerate(numbers):
            difference = target - num
            if difference in dictionary.keys():
                return [dictionary.get(difference), i+1]
            dictionary[num] = i+1