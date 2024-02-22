class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d={}
        aa=[]
        for i in range(1,n+1):
            d[i]=0
        for i in trust:
            a=i[0]
            aa.append(a)
            b=i[1]
            d[b]+=1
        
        for i in d.keys():
            if d[i]==n-1 :
                if i not in aa:
                    return i
        return -1
