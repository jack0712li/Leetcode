class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        people.sort(key = lambda x: (-x[0],x[1]) )
        result = []


        for each in people:
            result.insert(each[1],each)

        return result        