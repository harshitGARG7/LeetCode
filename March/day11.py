class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lo=[]
        ls=[]
        c=[]
        d={}
        ans=''
        uc=[]
        for i in s:
            ls.append(i)
        for i in order:
            lo.append(i)
        for i in lo:
            if i in ls:
                c.append(i)
        for i in ls:
            if i not in c:
                uc.append(i)
        for i in c:
            d[i]=ls.count(i)
        for i in c:
            ans+=i*d[i]
        for i in uc:
            ans+=i
        return ans
