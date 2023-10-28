def countGoodTriplets(arr,a,b,c):
    res =[]
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                #print(arr[i],arr[j],arr[k])
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    res.append([arr[i],arr[j],arr[k]])

    print(res)
    return len(res)

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
countGoodTriplets(arr,a,b,c)

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
countGoodTriplets(arr,a,b,c)