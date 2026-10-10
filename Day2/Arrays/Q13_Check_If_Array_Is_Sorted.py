##https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def isSorted(self, arr):
        
        for i in range(1,len(arr)):
           if arr[i] < arr[i-1]:
               return False
            
        return True
