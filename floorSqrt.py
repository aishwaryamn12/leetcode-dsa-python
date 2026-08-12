class Solution:
    def floorSqrt(self, n): 
        l=1
        r=n
        ans=[]
        while l<=r:
            mid=(l+r)//2
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans            
        
