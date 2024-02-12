class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        max=0
        n=0
        for i in d.keys():
            if d[i]>max:
                max=d[i]
                n=i
        return n
