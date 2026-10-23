class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative = 0
        count = 0
        seen = {0: 1}

        for num in nums:
            cumulative += num

            if cumulative - k in seen:
                count += seen[cumulative - k]

            seen[cumulative] = seen.get(cumulative, 0) + 1

        return count