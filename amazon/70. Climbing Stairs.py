class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n+1)

        dp[1]=1
        dp[2] =2

        for i in range(3,len(dp)):
            dp[i] = dp[i-1]+ dp[i-2]

        return dp[-1]
    
    class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        s1 = 1
        s2 = 2
        s3 = -1
        for i in range(3,n+1):
            s3 = s1 + s2
            s1= s2
            s2 = s3

        return s3




