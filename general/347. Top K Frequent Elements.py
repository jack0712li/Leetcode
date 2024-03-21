import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []

        coutner = {}

        for each in nums:
            coutner[each] = coutner.get(each,0) + 1

        for ele, freq in coutner.items():
            heapq.heappush(heap,(freq,ele))

            if len(heap) > k:
                heapq.heappop(heap)
        result = [0] * k 
        for each in range(k-1,-1,-1):
            result[each] = heapq.heappop(heap)[1]

        return result
        