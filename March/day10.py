class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i not in l and i in nums2:
                l.append(i)
        return l
