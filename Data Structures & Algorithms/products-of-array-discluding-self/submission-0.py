class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        pref = 1

        for i in range(len(nums)):
            output[i] = pref
            pref *= nums[i]
        suff = 1
        
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suff
            suff *= nums[i]
        return output