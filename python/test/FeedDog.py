

def feedDogHelper(hl,bs,i,j):
    if i == len(hl) or j == len(bs):
        return 0
    if bs[j] >= hl[i]:
        return 1 + feedDogHelper(hl,bs,i+1,j+1)
    else:
        return feedDogHelper(hl,bs,i,j+1)
def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()
    return feedDogHelper(hunger_level,biscuit_size,0,0)
    



hunger_level = [2,3] 
biscuit_size = [1,1]
hunger_level2 = [2, 1]
biscuit_size2 = [1,3,2]

print(feedDog(hunger_level,biscuit_size))