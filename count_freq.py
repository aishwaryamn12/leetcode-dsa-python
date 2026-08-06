class Solution:
    def firstOccurance(self, arr, target):
        n=len(arr)
        l=0
        r=n-1
        first=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                first=mid
                r=mid-1
            elif arr[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return first
    def lastOccurance(self, arr, target):
        n=len(arr)
        l=0
        r=n-1
        last=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                last=mid
                l=mid+1
            elif arr[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return last
    def countFreq(self,arr,target):
        first=self.firstOccurance(arr,target)
        if first==-1:
            return 0
        last=self.lastOccurance(arr,target)  
        return last-first+1
                
        
        
