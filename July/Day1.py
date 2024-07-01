#1550.py
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        t= False
        n=len(arr)
        for i in range(len(arr)):
            if arr[i]%2==1:
                if i!=n-2 and i!=n-1 and arr[i+1] %2==1 and arr[i+2]%2==1:
                    return True
        return False
