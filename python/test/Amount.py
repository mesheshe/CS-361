def amountHelper(a,s,i,c,r):
    if s == 0:
        if c not in r:
            arr = []
            for ele in c:
                arr.append(ele)
            r.append(arr)
        return
    if i == len(a): return
    if s - a[i] >= 0:
        c.append(a[i])
        amountHelper(a,s-a[i],i+1,c,r)
        c.pop()
    amountHelper(a,s,i+1,c,r)

def amount(A,S):
    r = []
    A.sort()
    amountHelper(A,S,0,[],r)
    return r




print(amount([11,1,3,2,6,1,5],8))