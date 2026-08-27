class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<=r:
            mid=(l+r)//2
            day=1
            capacity=0
            for weight in weights:
                if weight+capacity>mid:
                    day+=1
                    capacity=0
                capacity+=weight
            if day<=days:
                r=mid-1
            else:
                l=mid+1
        return l            

        
