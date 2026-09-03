class Solution:
    def minTime (self, arr, k):
         l=max(arr)
         r=sum(arr)
         while l<=r:
             mid=(l+r)//2
             painters=1
             total=0
             for board in arr:
                 if total+board>mid:
                     painters+=1
                     total=0
                 total+=board
             if painters<=k:
                 r=mid-1
             else:
                 l=mid+1
         return l                    

        
           
