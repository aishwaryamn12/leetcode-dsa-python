class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()

        for ch in s:
            if ch.isdigit():
                nums.add(int(ch))

        nums = sorted(nums, reverse=True)

        if len(nums) < 2:
            return -1
        
        return nums[1]
