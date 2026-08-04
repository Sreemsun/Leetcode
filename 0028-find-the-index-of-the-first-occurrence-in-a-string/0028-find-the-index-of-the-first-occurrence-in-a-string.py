class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        st =[]
        m = len(needle)
        for i in range(len(haystack)-m+1):
            if(haystack[i:i+m] == needle):
                return i
        return -1
