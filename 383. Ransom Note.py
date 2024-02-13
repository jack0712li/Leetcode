class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        recorder = {}
        # 记录每个字母出现次数
        for each in magazine:
            recorder[each] = recorder.get(each,0) +1

        for each in ransomNote:
            # 如果有则减一，如果没有则直接retrun flase
            if each in recorder:
                recorder[each] -= 1
                if recorder[each] == 0:
                    del recorder[each]
            else:
                return False

        return True
    
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # 理论上这种方式时间复杂度一样，但是空间应该更小，因为用链表
        recorder = [0] * 26

        for each in magazine:
            recorder[ord(each) - ord("a")] += 1
        
        for each in ransomNote:
            if recorder[ord(each)- ord("a")] == 0:
                return False
            else:
                recorder[ord(each)- ord("a")] -= 1

        return True
        