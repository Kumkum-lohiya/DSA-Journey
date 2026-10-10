##https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1

class Solution:
    def largest(self, arr):
        large = arr[0]
        for i in arr:
            if i >= large:
                large = i
          
        return large  
        
