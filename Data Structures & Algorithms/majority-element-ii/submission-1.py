class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = len(nums) // 3
        candidate1 = candidate2 = 0
        count1 = count2 = 0
        output = []

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        if nums.count(candidate1) > check:
            output.append(candidate1)
        
        if candidate2 != candidate1 and nums.count(candidate2) > check:
            output.append(candidate2)

        return output