class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        output = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if (count[num] > (len(nums) // 2) ):
                output = num
                break
        return output