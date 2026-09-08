class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(i):
            if i>= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            
            robcurrent = nums[i] + help(i+2)
            skipcurrent = help(i+1)
            dp[i] = max(robcurrent,skipcurrent)
            return dp[i]
        dp = [-1]*len(nums)
        return help(0)