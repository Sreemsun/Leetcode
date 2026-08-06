class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]*(len(gain)+1)
        m = 0
        i = 0
        for b in gain:
            a[i] = m + b
            m = a[i]
            i+=1
        return max(a)
        