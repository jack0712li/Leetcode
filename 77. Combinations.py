class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n,k,0,[],result)
        return result
        

    def backtracking(self,n,k,startIndex,path,result):
        if len(path) == k:
            result.append(path[:])

        for i in range(startIndex,n):
            path.append(i+1)
            self.backtracking(n,k,i+1,path,result)
            path.pop()
