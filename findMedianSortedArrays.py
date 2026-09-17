class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        n=len(arr)
        if n%2==1:
            return arr[n//2]
        else:
            mid=n//2
            return (arr[mid-1]+arr[mid])/2 

        
