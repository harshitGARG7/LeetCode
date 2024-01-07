class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_count = 0  
        dp = []
        ii=0
        for k in range(0,len(nums)):
            dp.append(defaultdict(int))
            ii=k
        answer=0
        for i in range(1, len(nums)):
            answer+=i
            for j in range(0,i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]
        return total_count
