class Solution:
    def trap(self, height: List[int]) -> int:
        m=0
        n=0
        l=len(height)
        if l<3:
            return 0
        a=[0]*l
        for i in range(l):
            m=max(m,height[i])
            a[i]=m
        b=[0]*l
        for j in range(l-1,-1,-1):
            n=max(n,height[j])
            b[j]=n
        w=0
        for i in range(l):
            w+=(min(a[i],b[i])-height[i])
        return w
