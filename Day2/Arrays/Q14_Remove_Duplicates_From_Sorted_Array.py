# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
       
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
