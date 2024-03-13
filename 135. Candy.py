class Solution:
    def candy(self, ratings: List[int]) -> int:
        vec = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings [i-1]:
                vec[i] = vec[i-1] + 1


        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                vec[i] = max(vec[i],vec[i+1] +1)

        return sum(vec)        