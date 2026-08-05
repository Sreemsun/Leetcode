class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        m = math.ceil(len(b)/len(a))

        if b in (a*m):
            return m
        if b in (a*(m+1)):
            return m+1
        return -1