class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps=0
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for j in t:
            if j not in d2:
                d2[j]=1
            else:
                d2[j]+=1
        for i in d1.keys():
            if i not in d2:
                steps+= d1[i]
            else:
                if d2[i]<d1[i]:
                    steps+=d1[i]-d2[i]
        return steps
