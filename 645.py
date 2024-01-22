class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        d={}
        for i in range(1,len(nums)+1):
            d[i]=0
        for i in nums:
            d[i]+=1
        gayab=0
        dobara=0
        for i in d.keys():
            if d[i]==2:
                dobara=i
            if d[i]==0:
                gayab=i
        return [dobara,gayab]
            
