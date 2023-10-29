def mergeSimilar(items1,items2):
    #print(items1,items2)
    itemDic = {}
    
    for i in range(0,len(items1)):
        #print(items1[i])
        #print(items1[i][0])
        #print(items1[i][1])
        if items1[i][0] in itemDic:
            itemDic[items1[i][0]]+=items1[i][1]
        else:
            itemDic[items1[i][0]] = items1[i][1]
    #FOR 2ND ITEM LISTS
    for i in range(0,len(items2)):
        if items2[i][0] in itemDic:
            itemDic[items2[i][0]]+=items2[i][1]
        else:
            itemDic[items2[i][0]] = items2[i][1]
        
    #print(itemDic)
    itemDic=dict(sorted(itemDic.items()))
    
    return [[num,count] for num,count in itemDic.items()]
    
        

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
mergeSimilar(items1,items2)

items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]
mergeSimilar(items1,items2)

items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
mergeSimilar(items1,items2)