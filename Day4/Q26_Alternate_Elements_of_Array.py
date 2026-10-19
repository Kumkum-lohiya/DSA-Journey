
class Solution:
    def getAlternates(self, arr):
        """
        Return alternate elements of an array,
        starting from the first element (index 0).
        """

        res = []

        # Traverse the array with a step size of 2
        for i in range(0, len(arr), 2):
            res.append(arr[i])

        # Return alternate elements
        return res
