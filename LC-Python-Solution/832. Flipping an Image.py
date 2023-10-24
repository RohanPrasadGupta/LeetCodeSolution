def flipAndInvertImage(image):
    res = [image[i][::-1] for i in range (0,len(image))]
    #for i in range (0,len(image)):
     #   res.append(image[i][::-1])
    
    for subArr in res:
        #print(subArr)
        for i in range (0,len(subArr)):
            #print(subArr[i])
            if subArr[i] == 1:
                subArr[i] = 0
            elif subArr[i] == 0:
                subArr[i] = 1
    return res


image = [[1,1,0],[1,0,1],[0,0,0]]
flipAndInvertImage(image)


image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
flipAndInvertImage(image)
