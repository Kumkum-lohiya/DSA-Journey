class Solution:
    def convertFive(self, n):
        ans = 0
        i = 0
        if n == 0:
            ans = 5
        while n > 0:
            rem = n % 10
            if rem == 0:
                rem = 5
            ans = rem * (10**i) + ans
            n = n//10
            i += 1
        return ans
            
            
            
        
