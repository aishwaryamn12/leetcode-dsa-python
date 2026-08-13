class Solution:
    def nthRoot(self, n, m):
        l=0
        r=m
        while l<=r:
            mid=(l+r)//2
            value=mid**n
            if value==m:
                return mid
            elif value<m:
                l=mid+1
            else:
                r=mid-1
        return -1        
