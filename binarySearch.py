class Solution:
    def binarySearch(self, arr, k):
        n=len(arr)
        for i in range(n):
            if arr[i]==k:
                return True
        return False
                
