class Solution:
    def find(self, arr, x):
        n=len(arr)
        l=0
        r=n-1
        first=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                first=mid
                r=mid-1
            elif arr[mid]<x:
                l=mid+1
            else:
                r=mid-1
        l=0
        r=n-1
        last=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                last=mid
                l=mid+1
            elif arr[mid]<x:
                l=mid+1
            else:
                r=mid-1
        return[first,last]        
