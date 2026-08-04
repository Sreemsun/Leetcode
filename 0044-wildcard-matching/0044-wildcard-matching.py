class Solution(object):
    def isMatch(self, s, p):
        n, m = len(s), len(p)

        prev = [False] * (m + 1)
        curr = [False] * (m + 1)

        prev[0] = True

        # Empty string vs pattern
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]

        for i in range(1, n + 1):
            curr[0] = False

            for j in range(1, m + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    curr[j] = prev[j - 1]
                elif p[j - 1] == '*':
                    curr[j] = curr[j - 1] or prev[j]
                else:
                    curr[j] = False

            prev = curr[:]
            curr = [False] * (m + 1)

        return prev[m]
        