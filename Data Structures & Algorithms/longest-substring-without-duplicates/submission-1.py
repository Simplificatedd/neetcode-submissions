class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        previous = set()
        left = 0
        max_count = 0
        for right in range(len(s)):
            while s[right] in previous:
                previous.remove(s[left])
                left += 1

            count = right - left + 1
            
            previous.add(s[right])
            max_count = max(max_count, count)
        return max_count