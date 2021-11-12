def dna_match_topdown(DNA1, DNA2, m = None, n = None, memo = None):
    if m is None:
        m, n, memo= len(DNA1)-1, len(DNA2)-1,{}
    key = (m,n)
    if key in memo: return memo[key]
    if m < 0 or n < 0: return 0
    if DNA1[m] == DNA2[n]: 
        memo[key] = 1 + dna_match_topdown(DNA1,DNA2,m-1,n-1,memo)
    else: 
        memo[key] = max(dna_match_topdown(DNA1,DNA2,m-1,n,memo),dna_match_topdown(DNA1,DNA2,m,n-1,memo))
    return memo[key]
m,n = 3,4
print([[0]*(n+1)]*(m+1) == [[0 for x in range(n+1)] for x in range(m+1)])#)
def dna_match_bottomup(DNA1, DNA2):
    m, n = len(DNA1), len(DNA2)
    memo = [[0 for x in range(n+1)] for x in range(m+1)]#[[-1]*(n+1)]*(m+1) #
    for i in range(len(DNA1)+1):
        for j in range(len(DNA2)+1): 
            if i == 0 or j == 0:
                memo[i][j] = 0   
            elif DNA1[i-1] == DNA2[j-1]: 
                memo[i][j] = 1 + memo[i-1][j-1]#dna_match_bottomup(DNA1,DNA2,i-1,j-1,memo)
            else: 
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])#dna_match_bottomup(DNA1,DNA2,i-1,j,memo), dna_match_bottomup(DNA1,DNA2,i,j-1,memo))
    return memo[m][n]

print(dna_match_bottomup("ATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAA","GTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAA"))
print(dna_match_bottomup("ATAGTTCCGTCAAA","GTGTTCCCGTCAAA"))
#answer = 12
