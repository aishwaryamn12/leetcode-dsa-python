class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        rank={}
        for i, num in enumerate(sorted_nums):
              if num not in rank:
                rank[num] = i
        result=[]
        for num in nums:  
            result.append(rank[num])  
        return result
