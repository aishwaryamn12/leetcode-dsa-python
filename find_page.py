class Solution:
    def findPages(self, arr, k):
        if k>len(arr):
            return -1
        l=max(arr)
        r=sum(arr)
        while l<=r:
            mid=(l+r)//2
            students=1
            pages=0
            for book in arr:
                if pages+book>mid:
                    
                    students+=1
                    pages=0
                pages+=book
            if students<=k:
                r=mid-1
            else:
                l=mid+1
        return l        
                
                
