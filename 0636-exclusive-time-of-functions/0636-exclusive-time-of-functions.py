class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        r =[0]*n
        s = []
        pt = 0

        for l in logs:
            id,t,time = l.split(':')
            id,time = int(id), int(time)
            if t == 'start':
                if s:
                    r[s[-1]] += time - pt
                s.append(id)
                pt = time
            else:
                r[s.pop()] += time - pt + 1
                pt = time+1
        return r