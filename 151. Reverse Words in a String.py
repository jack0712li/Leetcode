class Solution:
    def reverseWords(self, s: str) -> str:
        
        # 这里要注意的地方是要用默认的split函数去除所有空格包括开头和结尾的

        arr = s.split()

        newarr = arr[::-1]

        return ' '.join(newarr)