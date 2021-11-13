import heapq;
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
    if checkBounds(i, j+1, bounds):
        currNodes.append((i,j+1))
    if checkBounds(i-1, j, bounds):
        currNodes.append((i-1,j))
    if checkBounds(i, j-1, bounds):
        currNodes.append((i,j-1))
    if checkBounds(i+1, j, bounds):
        currNodes.append((i+1,j))
    return currNodes

def minEffortHelper(puzzle,memo,que, visited):
    ans = [0]
    tof = False
    while que:
        val,(i,j) = heapq.heappop(que)
        neighbors = getCurrNodes(i,j,len(puzzle))
        if i == len(puzzle)-1 and j == len(puzzle)-1:
            tof = True 
        if not tof:
            ans.append(1000)
        for (k,z) in neighbors:
            if (k,z) not in visited:
                visited.append((k,z))
                memo[k][z] = min(memo[k][z], abs(puzzle[k][z]-puzzle[i][j]))
                if not tof:
                    if ans[len(ans)-1] > memo[k][z]:
                        ans.pop()
                        ans.append(memo[k][z])
                heapq.heappush(que,(memo[k][z],(k,z)))
    while 1000 in ans:
        ans.remove(1000)
    print(ans)
    return max(ans)

def minEffort(puzzle):
    memo = [[1000 for j in range(len(puzzle))] for i in range(len(puzzle))]
    memo[0][0] = 0
    h = []
    heapq.heappush(h,(0,(0,0)))
    minEffortHelper(puzzle, memo,h,[(0, 0)])
    return memo

puzzle = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
"""
0,1,0
2,6,0
2,2,3
[1,2,2]
[3,8,2]
[5,3,5]
"""

print(minEffort(puzzle))