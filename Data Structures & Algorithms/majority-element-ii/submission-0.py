class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        diction = {}
        check = len(nums) / 3.0
        output = []
        outputcheck = False
        for num in nums:
            if num in diction:
                diction[num] += 1
            else:
                diction[num] = 1
            if diction[num] > check:
                outputcheck = True
                if num not in output:
                    output.append(num)
        
        return output if outputcheck else []