def largestAltitude(gain):
    #print (gain)
    res = [0]
    for i in range(0,len(gain)):
        gainLen = gain[i] + res[-1]
        res.append(gainLen)
    
    return max(res)
    
    
gain = [-5,1,5,0,-7]
largestAltitude(gain)

gain = [-4,-3,-2,-1,4,3,2]
largestAltitude(gain)