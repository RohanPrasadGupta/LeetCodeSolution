class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num==1:
            return True

        for i in range(1,(num//2)+1):
            if i*i ==num:
                return True
            elif i*i>num:
                return False
        
        return False



# ANOTHER SOLUTION


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l = 1
        r = num
        while l<=r:
            m = (l+r)//2

            if m*m < num:
                l = m+1

            elif m*m > num:
                r = m-1

            else:
                return True
        
        return False


        