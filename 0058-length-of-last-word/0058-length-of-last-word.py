class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        d = []
        return len(a[-1])