# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1#


class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_length = 0
        prefix_map = {}

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_length = max(max_length, i + 1)

            required = prefix_sum - k

            if required in prefix_map:
                length = i - prefix_map[required]
                max_length = max(max_length, length)

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_length
