class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i = 0
        mindf = float('inf')
        result = []

        for i in range(len(arr)-1):
            d = arr[i+1]-arr[i]
            if mindf>d:
                mindf = d
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == mindf:
                result.append([arr[i],arr[i+1]])
        return result