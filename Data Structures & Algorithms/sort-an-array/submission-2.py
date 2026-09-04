from random import randint
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quick sort
        n = len(nums)
        self.quickSort(nums, 0, n-1)
        return nums

    def partition(self, nums, low, high):
        pivot_index = randint(low, high)
        self.swap(nums, pivot_index, high)
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                self.swap(nums, i, j)
        self.swap(nums, i + 1, high)
        return i + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def quickSort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quickSort(nums, low, pi - 1)
            self.quickSort(nums, pi + 1, high)