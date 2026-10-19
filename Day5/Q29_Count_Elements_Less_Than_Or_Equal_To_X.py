
class Solution:
    def countOfElements(self, x, arr):
        """
        Count the number of elements in the array
        that are less than or equal to x.
        """

        count = 0

        # Traverse each element of the array
        for i in arr:
            if i <= x:
                count += 1

        # Return the total count
        return count
