class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        c = 0
        i = 0
        while i<len(nums):
            c = nums[i]-1
            if nums[i]<=len(nums) and nums[i]>0 and nums[c]!=nums[i] :
                nums[i],nums[c] = nums[c],nums[i]
            else:
                i+=1
        i=0
        while i<len(nums):
            if nums[i]==i+1:
                i+=1
            else:
                return i+1
        return i+1
