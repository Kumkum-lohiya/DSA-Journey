##https://www.geeksforgeeks.org/problems/palindrome0746/1

class Solution:
    def isPalindrome(self, n):
        n = abs(n)
        original_num = n
        rev = 0

        while n > 0:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10

        return original_num == rev
