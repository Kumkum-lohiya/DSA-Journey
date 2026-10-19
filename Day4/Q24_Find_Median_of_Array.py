
class Solution:
    def findMedian(self, arr):
        """
        Find the median of an array after sorting it.

        Args:
            arr: A non-empty list of numbers.

        Returns:
            The middle element for odd-length arrays,
            or the average of the two middle elements
            for even-length arrays.
        """

        n = len(arr)

        # Sort the array in ascending order
        arr.sort()

        # Odd number of elements
        if n % 2 != 0:
            median = arr[n // 2]

        # Even number of elements
        else:
            median = (arr[n // 2 - 1] + arr[n // 2]) / 2

        return median
