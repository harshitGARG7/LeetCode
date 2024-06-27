class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        one=edges[0][0]
        two=edges[0][1]
        t=edges[1][0]
        f=edges[1][1]
        if one==t:
            return t
        if one==f: 
            return f
        if two==t:
            return t
        else:
            return f
        
