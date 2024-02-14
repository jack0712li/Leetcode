class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        
        # 写一个专门反转list的函数

        def reverse(s:list):
            return s[::-1]
        
        news = list(s)
        
        # 每次走2k步数，反转前k个list

        for i in range(0,len(s),2*k):
            news[i:i+k] = reverse(news[i:i+k])
        
        # 最后把list join成str
        return ''.join(news)
        