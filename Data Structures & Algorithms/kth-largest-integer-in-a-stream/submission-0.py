class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]