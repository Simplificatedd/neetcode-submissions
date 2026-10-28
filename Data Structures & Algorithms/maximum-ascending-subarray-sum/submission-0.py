class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        cum_sum = 0
        previous = 0
        for num in nums:
            if num > previous:
                cum_sum += num
            else:
                cum_sum = num
            
            max_sum = max(max_sum, cum_sum)
            previous = num

        return max_sum