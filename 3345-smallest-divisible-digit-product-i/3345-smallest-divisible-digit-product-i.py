class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        c = True
        k = n
        
        while c:
            p = 1
            m = k
            while m>0:
                v = m%10
                m = m//10
                p = p*v
            if p%t==0:
                return k
            k+=1
               


