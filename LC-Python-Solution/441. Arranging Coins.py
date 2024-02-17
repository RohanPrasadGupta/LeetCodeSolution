class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 1
        while (i<=n):
            count+=1
            n-=i
            i+=1
        return count




        