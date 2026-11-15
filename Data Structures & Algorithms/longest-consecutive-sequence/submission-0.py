class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        
        for j in s:
            if j-1 not in s:
                len = 1
                while j + len in s:
                    len+=1
                longest = max(longest, len)
        return longest