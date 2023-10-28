def sumZero(n):
    res = []
    temp = int(n/2)

    if n%2!=0:
        res.append(0)
        
    for i in range(1,temp+1):
        res.append(i)
        res.append(-i)
        
    return res


n = 5
sumZero(n)

n = 3
sumZero(n)

n = 1
sumZero(n)