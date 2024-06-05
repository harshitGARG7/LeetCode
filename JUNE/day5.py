#dpp 1002

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = [
            "q",
            "w",
            "e",
            "r",
            "t",
            "y",
            "u",
            "i",
            "o",
            "p",
            "a",
            "s",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "z",
            "x",
            "c",
            "v",
            "b",
            "n",
            "m",
        ]
        ans = []
        for i in l:
            a = False
            for j in words:
                if i not in j:
                    a = True
                    break
            if a == False:
                ans.append(i)
        final = []
        for i in ans:
            maxx = []
            for j in words:
                maxx.append( j.count(i))
                # maxx = min(maxx, x)
            x=maxx[0]
            for k in range(1,len(maxx)):
                x=min(x,maxx[k])
            for m in range(x):
                final.append(i)
        return final
