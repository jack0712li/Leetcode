class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        self.backtracking(s,0,[],result)

        return result
        


    def backtracking(self,s,startIndex,path,result):

        if startIndex == len(s):
            result.append(path[:])
            return
        
        for i in range(startIndex,len(s)):

            if self.isPalindrome(s,startIndex,i):

                path.append(s[startIndex:i+1])
                self.backtracking(s,i+1,path,result)
                path.pop()



    
    def isPalindrome(self,s , start, end):


        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
        
