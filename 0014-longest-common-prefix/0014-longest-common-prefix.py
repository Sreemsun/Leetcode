class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        mn = len(strs[0])
        m =strs[0]
        cnt =0
        for val in strs:
            if mn >len(val):
                mn = len(val)
                m = val
        for val in strs:
            while not val.startswith(m):
                m = m[:-1]
                if not m:
                    return ""
        return m
                

        