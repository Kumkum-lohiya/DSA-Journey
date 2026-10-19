
class Solution:
    def findMean(self, arr):
        """
        Calculate the floor mean of a non-empty array.

        Args:
            arr: List of integers.

        Returns:
            Integer mean of the array, rounded down.
        """

        total = 0
        n = len(arr)

        # Calculate the sum of all elements
        for num in arr:
            total += num

        # Calculate the floor mean
        mean = total // n

        return mean
