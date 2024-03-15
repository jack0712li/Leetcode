class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        self.backtracking(n,"",result,0,0)
        return result
        
    
    def backtracking(self, n,path,result,left,right):
        if len(path) == 2* n:
            result.append(path)
            return 
        if left < n:
            self.backtracking(n,path+"(",result,left+1,right)

        if right < left:
            self.backtracking(n,path+")",result,left,right+1)
        

