#Day1 2864 : problem solved
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        for i in s:
            one=s.count('1')
            zero=s.count('0')
        a='1'
        one-=1
        a=zero*'0'+a
        a=one*'1'+a
        return a
