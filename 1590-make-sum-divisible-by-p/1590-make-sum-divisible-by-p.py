class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        r = s%p
        min_len = len(nums)
        if r == 0:
            return 0
        d = {None:None}
        d = {0:-1}
        rem = 0
        for i, num in enumerate(nums):
            rem = (rem + num)%p
            nr = (rem -r+p)%p
            if nr in d:
                min_len = min(min_len, i - d[nr])
            d[rem] = i
        if min_len == len(nums):
            return -1
        else:
            return min_len

            
