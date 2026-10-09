##https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

class Solution:
    def sumOfSeries(self,n):
        sum = int(pow(((n *(n + 1))/2),2))
        return sum
