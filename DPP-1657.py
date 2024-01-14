class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        for i in word2:
            if i not in word1:
                return False
        for i in word1:
            if i not in word2:
                return False
        d1={}
        d2={}
        for i in word1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in word2:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        l1=[]
        l2=[]
        for i in d1.keys():
            l1.append(d1[i])
        for i in d2.keys():
            l2.append(d2[i])
        l1.sort()
        l2.sort()
        if l1!=l2:
            return False
        return True
