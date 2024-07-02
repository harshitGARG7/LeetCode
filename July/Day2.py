# 350.py

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=[]
        for i in nums1:
            if i  in nums2 and i not in c:
                c.append(i)
        ans=[]
        for i in c:
            a=nums1.count(i)
            b=nums2.count(i)
            m=min(a,b)
            for j in range(m):
                ans.append(i)
        return ans
