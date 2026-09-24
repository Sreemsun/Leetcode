class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        s = 0
        t = 0
        a = [0] * len(nums)
        for i in range(len(nums)):
            cnt = len(str(abs(nums[i])))
            n = nums[i]
            s = 0
            if cnt > 1:
                while n > 0:
                   t = n % 10
                   s = s + t
                   n = n//10
                a[i] = s
            else:
                a[i] = n
        for i in range(len(a)):
            if a[i] == i:
                return i               
        return -1


        