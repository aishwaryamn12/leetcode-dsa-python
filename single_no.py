class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for num in nums:
            ans^=num
        return ans        
