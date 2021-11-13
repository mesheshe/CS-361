import heapq;
"""
BFS: [A, B, D, F, G, C, E]
DFS: [A, B, F, C, E, D, G]
"""

def checkBounds(i,j,boundX, boundY):
    if i >= 0 and i < boundX:
        if j >= 0 and j < boundY:
            return True
    return False 

def getNeighbors(i,j,puzzle):
    neighbors = {}
    neighbors[(i,j)] = {}
    if checkBounds(i, j+1, len(puzzle), len(puzzle[0])):
        neighbors[(i,j)][(i,j+1)] = abs(puzzle[i][j]-puzzle[i][j+1])
    if checkBounds(i-1, j, len(puzzle), len(puzzle[0])):
        neighbors[(i,j)][(i-1,j)] = abs(puzzle[i][j]-puzzle[i-1][j])
    if checkBounds(i, j-1, len(puzzle), len(puzzle[0])):
        neighbors[(i,j)][(i,j-1)] = abs(puzzle[i][j]-puzzle[i][j-1])
    if checkBounds(i+1, j, len(puzzle), len(puzzle[0])):
        neighbors[(i,j)][(i+1,j)] = abs(puzzle[i][j]-puzzle[i+1][j])
    return neighbors[(i,j)]

def populateEffort(boundX, boundY):
    effort = {}
    for i in range(boundX):
        for j in range(boundY):
            effort[(i,j)] = 100000000000
    return effort

def puzzle2graph(puzzle):
    graph = {}
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            graph[(i,j)] = getNeighbors(i,j,puzzle)
    return graph  

def minEffortHelper(puzzle,start,effort):
    que = [(effort[start], start)]
    while que:
        currEffort, currCoord = heapq.heappop(que)

        for neighbor, localWeight in puzzle[currCoord].items():
            tempWeight = max(currEffort,localWeight)

            if tempWeight < effort[neighbor]:
                effort[neighbor] = tempWeight
                heapq.heappush(que, (tempWeight, neighbor))

def minEffort(puzzle):
    effort = populateEffort(len(puzzle), len(puzzle[0]))
    effort[(0,0)] = 0
    minEffortHelper(puzzle2graph(puzzle), (0, 0),effort)
    print(puzzle)
    return effort[(len(puzzle) - 1,len(puzzle[0]) - 1)]

puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
"""
0,1,0
2,6,0
2,2,3
[1,2,2]
[3,8,2]
[5,3,5]
"""

#print(minEffort(puzzle))