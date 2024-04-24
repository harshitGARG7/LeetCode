class Solution:
    def tribonacci(self, n: int) -> int:
        a=[0,1,1]
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        for i in range(3,n+1):
            a.append(a[n-1]+a[n-2]+a[n-3])
            return a[n]
