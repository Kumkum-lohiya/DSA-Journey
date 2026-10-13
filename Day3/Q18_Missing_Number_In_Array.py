##https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        expected_sum = (n*(n+1))//2
        actual_sum = sum(arr)
        
        missing = expected_sum - actual_sum
        
        return missing
