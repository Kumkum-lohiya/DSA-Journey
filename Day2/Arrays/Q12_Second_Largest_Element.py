##https://www.geeksforgeeks.org/problems/second-largest3735/1

class Solution:
    def getSecondLargest(self, arr):
        # code here
        large = -1
        second_large = -1
        
        for i in arr:
            if i > large:
                second_large = large
                large = i
            elif i > second_large and i < large:
                second_large = i
            
        return second_large
                
