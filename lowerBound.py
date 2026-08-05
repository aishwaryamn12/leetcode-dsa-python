class Solution:
    def lowerBound(self, arr,target):
        n=len(arr)
        l=0
        r=n-1
        ans=n
        while l<=r:
            mid=(l+r)//2
            if arr[mid]>=target:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans        
