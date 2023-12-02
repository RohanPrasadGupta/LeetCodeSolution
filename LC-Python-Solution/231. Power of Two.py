class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n<=0:
            return False
        elif n==1:
            return True
        elif (n%2==0):
            return self.isPowerOfTwo(n//2)
        
        return False


# NORMAL SOLUTION

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n ==1:
            return True
        
        count = 1

        while count < n:
            count *= 4
        
        return (count == n)
        