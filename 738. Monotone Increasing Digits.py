class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        str_n = list(str(n))


        for i in range(len(str_n)-1,0,-1):
            if str_n[i] < str_n[i-1]:
                str_n[i-1]= str(int(str_n[i-1])-1)
                str_n[i:] = "9" *(len(str_n)-i )

        return int(''.join(str_n))
        