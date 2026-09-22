class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        longest = 0
        for num in nums:
            hashset.add(num)
        for num in hashset:
            if num - 1 not in hashset:
                current = num
                count = 1

                while current + 1 in hashset:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest