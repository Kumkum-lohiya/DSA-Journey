
class Solution:
    def palindrom(self, n):
        """
        Check whether a non-negative integer is a palindrome.
        """
        original = n
        reverse = 0

        # Reverse the digits of the number
        while n > 0:
            rem = n % 10
            reverse = reverse * 10 + rem
            n = n // 10

        # Compare reversed number with original
        if reverse == original:
            return True
        else:
            return False

    def isPalinArray(self, arr):
        """
        Return True if every element in the array
        is a palindrome number; otherwise False.
        """
        n = len(arr)
        count = 0

        # Count palindrome numbers in the array
        for i in arr:
            if self.palindrom(i):
                count += 1

        # Check whether all elements are palindromes
        if count == n:
            return True
        else:
            return False
