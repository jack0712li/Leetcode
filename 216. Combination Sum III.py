class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        self.backTracking(k,n,0,0,[],result)

        return result


    def backTracking(self,k,n,currentsum,index,path,result):

        if currentsum > n:
            return
        
        if len(path) == k:
            if currentsum == n:
                result.append(path[:])
            return

        for i in range(index+1,10):
            path.append(i)
            currentsum += i
            self.backTracking(k,n,currentsum,i,path,result)
            currentsum -= i
            path.pop()
        