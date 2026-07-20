class Solution:
    def majorityElement(self,nums:list[int])->None:
        maxi = nums[0]
        for num in nums:
            if num > maxi:
                 maxi = num
        return maxi
