"""
BFS: [A, B, D, F, G, C, E]
DFS: [A, B, F, C, E, D, G]
"""

def checkBounds(i,j,bound):
    if i >= 0 and i < bound:
        if j >= 0 and j < bound:
            return True
    return False 

def getCurrNodes(i,j,bounds):
    currNodes = []
    if checkBounds(i, j-1, bounds):
        currNodes.append((i,j-1))
    if checkBounds(i, j+1, bounds):
        currNodes.append((i,j+1))
    if checkBounds(i-1, j, bounds):
        currNodes.append((i-1,j))
    if checkBounds(i+1, j, bounds):
        currNodes.append((i+1,j))
    return currNodes

def minEffortHelper(puzzle,memo,i,j, visited):
    if i == len(puzzle) - 1 and j == len(puzzle)-1:
        print(memo)
        return 
    elif (i,j) not in visited:
        currNodes = getCurrNodes(i,j,len(puzzle))
        visited.append((i,j))
        for (k,z) in currNodes:
            memo[k][z] = min(memo[k][z], abs(puzzle[k][z]-puzzle[i][j]))
            minEffortHelper(puzzle,memo,k,z,visited)
    
def minEffort(puzzle):
    memo = [[1000 for j in range(len(puzzle))] for i in range(len(puzzle))]
    memo[0][0] = 0
    minEffortHelper(puzzle, memo, 0, 0,[])

puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]

"""
0,2,2
1,4,2
1,1,1

[1,3,5]
[2,8,3]
[3,4,5]
"""

minEffort(puzzle)