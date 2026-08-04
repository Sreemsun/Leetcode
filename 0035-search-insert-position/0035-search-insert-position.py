class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        t=0
        for i in range(len(nums)):
            if(nums[i]>=target):
                return i
        return len(nums)
