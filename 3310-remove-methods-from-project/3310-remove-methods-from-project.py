class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
        sus = [False]*n
        sus[k] = True
        queue = deque([k])

        while queue:
            c = queue.popleft()
            for a in graph[c]:
                if not sus[a]:
                    sus[a] = True
                    queue.append(a)
        for u,v in invocations:
            if not sus[u] and sus[v]:
                return list(range(n))
        return [i for i in range(n)if not sus[i]]
        
