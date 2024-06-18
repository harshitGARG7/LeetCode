class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        current_max_profit = 0
        j = 0
        
        for ability in worker:
            while j < len(jobs) and jobs[j][0] <= ability:
                current_max_profit = max(current_max_profit, jobs[j][1])
                j += 1
            max_profit += current_max_profit
        
        return max_profit
