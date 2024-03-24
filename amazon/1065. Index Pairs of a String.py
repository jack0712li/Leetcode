class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        word= set(words)
        result = []

        for i in range(len(text)):
            for j in range(i,len(text)):
                if text[i:j+1] in word:
                    result.append([i,j])

        

        return result
        