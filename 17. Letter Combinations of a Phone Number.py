class Solution:

    def __init__(self):
            self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
            self.result = []
            self.path = ''

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0:
            return []


        self.backtracking(digits,0)

        return self.result

    def backtracking(self,digits,index):

        if len(self.path) == len(digits):
            self.result.append(self.path)
            return

        digit = int(digits[index])
        letters = self.letterMap[digit]

        for i in range(len(letters)):
            self.path += letters[i]
            self.backtracking(digits,index+1)
            self.path = self.path[:-1]
        