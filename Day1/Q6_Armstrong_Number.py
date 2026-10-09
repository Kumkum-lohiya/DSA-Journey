##https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
class Solution:
    def armstrongNumber(self, n):
        original_num = n
        cube = 0

        while n > 0:
            rem = n % 10
            cube = cube + pow(rem, 3)
            n = n // 10

        return original_num == cube
