class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 + nums2
        arr.sort()

        n = len(arr)

        # Odd length
        if n % 2 == 1:
            return arr[n // 2]

        # Even length
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
