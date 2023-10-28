def DestinationCity(paths):
    outGoing = set()
    inComing = set()

    for x in paths:
        outGoing.add(x[0])
        inComing.add(x[1])

    for i in inComing:
        if i not in outGoing:
            return i
    
    
    #print("OUT: ",outGoing)
    #print("IN: ",inComing)

    
paths = [["B","C"],["D","B"],["C","A"]]
DestinationCity(paths)

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
DestinationCity(paths)

paths = [["A","Z"]]
DestinationCity(paths)
