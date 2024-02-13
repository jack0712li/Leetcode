class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        recorder = {}
        
        for n1 in nums1:
            for n2 in nums2:
                # 记录所有n1 n2相加的可能性
                recorder[n1+n2] = recorder.get(n1+n2,0) +1
                
        count = 0
        
        for n3 in nums3:
            for n4 in nums4:
                target = -(n3 + n4)
                
                # 如果n3 n4相加的复数存在于 n1+n2中意味着这是一个结果
                if target in recorder:
                    count += recorder[target]                
                
                
        return count