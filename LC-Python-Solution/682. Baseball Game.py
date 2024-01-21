class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []

        for item in operations:
            if item == '+':
                temp = res[-1]+res[-2]
                res.append(temp)
            
            elif item == 'D':
                temp = res[-1]*2
                res.append(temp)
            
            elif item == 'C':
                res.pop()
            
            else:
                res.append(int(item))
                
        return sum(res)
            




        