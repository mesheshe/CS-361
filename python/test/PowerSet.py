def powersetHelper(arr,i,choice, result):
    if i == len(arr): 
        a = []
        for e in choice: a.append(e)
        result.append(a); return 
    choice.append(arr[i])
    powersetHelper(arr,i+1,choice, result)
    choice.pop()
    powersetHelper(arr,i+1,choice,result)

def powerset(arr):
    result = []
    powersetHelper(arr,0,[], result)
    return result

print(powerset([1,2,3]))

