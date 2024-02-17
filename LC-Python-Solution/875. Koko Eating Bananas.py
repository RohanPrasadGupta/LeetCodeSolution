class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r

        def canEat(cap):
            hours = 0
            for pile in piles:
                hours += (pile + cap - 1) // cap  ``
            return hours <= h

        while l<=r:
            cap = l + (r-l)//2
            if canEat(cap):
                res = min(res,cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res



        




        