class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for integer in nums:
            count[integer] = count.get(integer, 0) + 1

        sorted_count = sorted(count, key=count.get, reverse=True)

        return sorted_count[:k]
