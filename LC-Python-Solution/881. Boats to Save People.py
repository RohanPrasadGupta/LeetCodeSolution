class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        n = len(people)
        res = []

        while l<=r:
            if people[r]==limit:
                res.append([people[r]])
                r-=1
            
            elif people[l]+people[r]>limit and people[r]<limit:
                res.append([people[r]])
                r-=1
            
            elif people[l]+people[r]<=limit:
                res.append([people[l],people[r]])
                l+=1
                r-=1
        
        return len(res)




        