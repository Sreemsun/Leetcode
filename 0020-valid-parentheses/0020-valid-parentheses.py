class Solution:
    def isValid(self, s: str) -> bool:
        x = []        
        j = 0

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                x.append(s[i])
                j += 1
            else:
                if j == 0:
                    return False
                if (s[i] == ")" and x[-1] != "(") or \
                   (s[i] == "}" and x[-1] != "{") or \
                   (s[i] == "]" and x[-1] != "["):
                    return False
                x.pop()
                j -= 1

        return j == 0