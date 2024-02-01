class Solution:
    def divideArray(self, nums, k):
        result=[]
        if len(nums) % 3 != 0:
            return l
        nums.sort()
        for i in range(0, len(nums), 3):
            if i + 2 < len(nums) and nums[i + 2] - nums[i] <= k:
                a=nums[i]
                b=nums[i + 1]
                c=nums[i + 2]
                result.append([a,b,c])
            else:
                return []
        return result
