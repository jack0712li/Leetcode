class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        real_s =[]
        real_t=[]

        for i in s:
            if i != "#":
                real_s.append(i)
            elif real_s:
                real_s.pop()


        for j in t:
            if j != "#":
                real_t.append(j)
            elif real_t:
                real_t.pop()

        return real_s == real_t