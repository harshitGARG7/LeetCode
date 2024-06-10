class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        b=[]
        for i in heights:
            b.append(i)
        b.sort()
        ans=0
        for i in range(len(heights)):
            if heights[i]!=b[i]:
                ans+=1
        return ans
