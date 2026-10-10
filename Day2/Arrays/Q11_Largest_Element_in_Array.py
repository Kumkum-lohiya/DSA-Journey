##https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1

class Solution:
    def largest(self, arr):
        max = 0
        for i in arr:
            if i >= max:
                max = i
          
        return max  
        
