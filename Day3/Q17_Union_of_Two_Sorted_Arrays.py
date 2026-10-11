#https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1

class Solution:
    def findUnion(self, a, b):
        i = 0
        j = 0
        n = len(a)
        m = len(b)

        result = []

        while i < n and j < m:
            if a[i] < b[j]:
                val = a[i]
                i += 1

            elif a[i] > b[j]:
                val = b[j]
                j += 1

            else:
                val = a[i]
                i += 1
                j += 1

            if not result or result[-1] != val:
                result.append(val)

        while i < n:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        while j < m:
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j += 1

        return result
