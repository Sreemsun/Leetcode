class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a =[]
        nums.sort()
        min = nums[0]
        max = nums[-1]
        j = min
        i=0
        while j<=max:
            if nums[i] != j:
                a.append(j)
            else:
                i+=1
            j+=1
        return a



            