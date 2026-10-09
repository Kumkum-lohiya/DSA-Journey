##https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1
class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b

        return a
