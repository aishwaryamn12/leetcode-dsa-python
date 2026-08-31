class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()
        l=0
        r=arr[-1]-arr[0]
        ans=0
        while l<=r:
            mid=(l+r)//2
            cow=1
            last=arr[0]
            for i in range(1,len(arr)):
                if arr[i]-last>=mid:
                    cow+=1
                    last=arr[i]
            if cow>=k:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans        
        
