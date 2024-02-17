class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ship = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ship+=1
                    currCap = cap
                currCap -=w
            return ship<=days

        while l<=r:
            cap = l + (r-l)//2
            if canShip(cap):
                res = min(cap,res)
                r = cap - 1            
            else:
                l = cap + 1
        
        return res






        