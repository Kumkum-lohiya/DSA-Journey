##https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = abs(n)
        ans = 1.0

        while num > 0:
            if num % 2 == 1:
                ans = ans * x

            x = x * x
            num = num // 2

        if n < 0:
            ans = 1 / ans

        return ans
