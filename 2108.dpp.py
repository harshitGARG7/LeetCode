class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            n = len(i)
            flag=True
            for k in range(0,n//2):
                if i[k]!=i[n-1-k]:
                    flag=False
            if flag:
                return i
        return ""
                
