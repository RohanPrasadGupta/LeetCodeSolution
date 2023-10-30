def sortPeople(names,heights):
    print(names)
    print(heights)
    peopleName = {}
    for i in range(0,len(names)):
        peopleName[names[i]] = heights[i]
    
    print(peopleName)
    print(peopleName)
    
    for i in range(0,len(names)):
        for j in range(i+1,len(names)):
            if heights[i]>heights[j]:
                heights[j] , heights[i] = heights[i] ,heights[j]
                names[j] , names[i] = names[i] , names[j]
    
    print(heights)
    print(names)
    return names[::-1]
    
    

    
names = ["Mary","John","Emma"]
heights = [180,165,170]
sortPeople(names,heights)