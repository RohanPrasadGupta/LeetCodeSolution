def countPoints(rings):
    #print(rings)
    ringRod = dict()
    
    for i in range(0,len(rings),2):
        color = rings[i]
        rod = rings[i+1]
        if rod in ringRod:
            ringRod[rod] += color
        else:
            ringRod[rod] = color
        
    #print(ringRod)
    count = 0
    #res = []
    for i in ringRod:
        #print(ringRod[i])
        if ('R' in ringRod[i] and 'B' in ringRod[i] and 'G' in ringRod[i] ):
            #res.append([i , ringRod[i]])
            count = count + 1 
    
    #print(res)
    return (count)
    
    
rings = "B0R0G0R9R0B0G0"
countPoints(rings)