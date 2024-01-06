class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(endTime, startTime, profit))
        jobs.sort()
        table = [0] * n
        table[0] = jobs[0][2]
        for i in range(1, n):
            incl_prof = jobs[i][2]
            l = -1
            lo, hi = 0, i - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if jobs[mid][0] <= jobs[i][1]:
                    l = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            if l != -1:
                incl_prof += table[l]
            table[i] = max(incl_prof, table[i - 1])
        return table[n - 1]
