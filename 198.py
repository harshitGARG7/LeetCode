class Solution(object):
    def rob(self, nums):
        rob=0 
        norob = 0
        for i in nums:
            newRob = norob + i
            newNoRob = max(norob, rob)
            rob, norob = newRob, newNoRob
        return max(rob, norob)
