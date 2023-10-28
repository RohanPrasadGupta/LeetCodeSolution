def countNegatives(grid):
    #print(grid)
    count = 0
    for subArr in grid:
        #print(subArr)
        for ele in subArr:
            if ele<0:
                count+=1
    
    return count


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
countNegatives(grid)

