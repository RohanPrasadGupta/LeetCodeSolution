def rowAndMaximumOnes(mat):
    #print(mat)
    numCount = dict()
    for i in range(0,len(mat)):
        count = 0
        for intr in mat[i]:
            if intr==1:
                count+=1
        numCount[i] = count
    #print(numCount)
    
    numCount = dict(sorted(numCount.items(), key=lambda item: item[1] , reverse=True))
    #print(numCount)
    
    for item,val in numCount.items():
        return ([item,val])
    

#ANOTHER SOLUTION
def rowAndMaximumOnes(mat):
    maxCount = -1
    maxRow = -1
    
    for i , row in enumerate(mat):
        oneCount = row.count(1)
        print(i,row,oneCount)
        
        if oneCount > maxCount:
            maxCount = oneCount
            maxRow = i
    
    return ([maxRow,maxCount])
        

mat = [[0,1],[1,0]]
rowAndMaximumOnes(mat)

mat = [[0,0,0],[0,1,1]]
rowAndMaximumOnes(mat)

mat = [[0,0],[1,1],[0,0]]
rowAndMaximumOnes(mat)