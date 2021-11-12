def check(i,j,puzzle):
    if i < 0 or i >= len(puzzle):
        return False
    if j < 0 or j >= len(puzzle):
        return False 
    if puzzle[i][j] == 0:
        return False
    return True 
def rT(puzzle,i,j,visited,goal,ans):
    if (i,j) == goal:
        ans[0] = True
        return
    #going left 
    if check(i-1,j,puzzle) and (i-1,j) not in visited:
        visited.append((i-1,j))
        rT(puzzle,i-1,j,visited,goal,ans)
    #going right
    if check(i+1,j,puzzle) and (i+1,j) not in visited:
        visited.append((i+1,j))
        rT(puzzle,i+1,j,visited,goal,ans)
    #going down
    if check(i,j-1,puzzle) and (i,j-1) not in visited:
        visited.append((i,j-1))
        rT(puzzle,i,j-1,visited,goal,ans)
    #going up
    if check(i,j+1,puzzle) and (i,j+1) not in visited:
        visited.append((i,j+1))
        rT(puzzle,i,j+1,visited,goal,ans)


def reachTreasure(puzzle):
    arr = [False]
    rT(puzzle,0,0,[(0,0)],(len(puzzle)-1,len(puzzle)-1),arr)
    return arr[0]



print(reachTreasure([[1, 0, 0,0],[1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 1,1]]))
