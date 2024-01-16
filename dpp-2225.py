class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        for i in matches:
            if i[1] not in d:
                d[i[1]]=1
            else:
                d[i[1]]+=1
            if i[0] not in d:
                d[i[0]]=0
        L1=[]
        L2=[]
        for i in d.keys():
            if d[i]==0:
                L1.append(i)
            if d[i]==1:
                L2.append(i)
        # for i in d.keys():
            # print("key : "+ str(i)+ " values : "+ str(d[i]))
        L1.sort()
        L2.sort()
        return [L1,L2]
