class Solution:
    def maskPII(self, s: str) -> str:
        c = ""
        if '@' in s:
            s = s.lower()
            n,f = s.split('@')
            c = n[0] + "*****" + n[-1] + "@" + f
            return c
        else:
            d =[]
            for b in s:
                if b.isdigit():
                    d.append(b)
            last = "" .join(d[-4:])
            mask = "***-***-" + last
            e = len(d) - 10

            if e == 0:
                return mask
            elif e == 1:
                return "+*-" + mask
            elif e == 2:
                return "+**-" + mask
            elif e == 3:
                return "+***-" + mask
