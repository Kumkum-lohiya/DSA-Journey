##https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        
        for i in range(2,n+1):
            next_num = a + b
            a = b
            b = next_num

        return next_num
        

            

        
        
