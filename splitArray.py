class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(arr)
        r=sum(arr)
        while l<=r:
            mid=(l+r)//2
            subarray=1
            total=0
            for num in nums:
                if total+num>mid:
                    subarray+=1
                    total=0
                total+=num
            if subarray<k:
                r=mid-1
            else:
                l=mid+1
        return l                    
        
