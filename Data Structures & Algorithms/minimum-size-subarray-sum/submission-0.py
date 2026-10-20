class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_length = len(nums) + 1

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_length = min(min_length, (right - left + 1) )
                total -= nums[left]
                left += 1

        if min_length == (len(nums) + 1):
            return 0
        else:
            return min_length