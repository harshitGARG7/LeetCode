class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(0,len(words)):
            if x in words[i]:
                ans.append(i)
        return ans
