class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        n=n%k
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])

        
