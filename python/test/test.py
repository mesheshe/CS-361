def func(arr):
    i, result, endVal = 0, 0, len(arr)
    while i < endVal:# in range(endVal):
        if arr[i] == 1:
            result += arr[i]
        else:
            if len(arr) != i + 1 and arr[i+1] != 1:
                result += (arr[i]*arr[i+1])
                i+= 1
            else:
                result += arr[i]
        i+= 1
    return result

def rodCutting_naive(n, prices):
    result = 0
    if n <= 0:
        return 0
    else:
        for i in range(1,n+1):
            # comparing between making the cut or not making it
            result = max(result, prices[i-1] + rodCutting_naive(n-i,prices))
    return result

#print(rodCutting_naive(4, [1,5,8,9,10]))

"""
base case 

if str == 0: return 0;
if match: 1 + func(substring)
if no match: 
"""


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

def dna_match_bottomup_helper():
    pass
def dna_match_bottomup(DNA1, DNA2, m = None, n = None, memo = None):
    if m is None:
        m, n, memo= 0, 0,[]
    key = (m,n)
    
    if DNA1[m] == DNA2[n]: 
        memo[key] = 1 + dna_match_topdown(DNA1,DNA2,m-1,n-1,memo)
    else: 
        memo[key] = max(dna_match_topdown(DNA1,DNA2,m-1,n,memo),dna_match_topdown(DNA1,DNA2,m,n-1,memo))

#print(dna_match_topdown("ATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAAATAGTTCCGTCAAA","GTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAAGTGTTCCCGTCAAA"))
#print(dna_match_bottomup("ATAGTTCCGTCAAA","GTGTTCCCGTCAAA"))
#answer = 12


#print(func([1, 2, 1]))

"""
You are playing a puzzle. A random number N is given, you have blocks of 
length 1 unit and 2 units. You need to arrange the blocks back to back 
such that you get a total length of N units. In how many distinct ways 
can you arrange the blocks for given N
"""
#[2,3,4,5]  9
def fhelp(nums, target,choices, i):
    if sum(choices) == target: print(choices); return    
    if sum(choices) > target:
        return
    for j in range(i,len(nums)):
        choices.append(nums[j])
        fhelp(nums,target,choices,j)
        choices.pop()


def func(nums,target):
    fhelp(nums, target, [], 0)

print(func([2,3,4,5],9))
 
 
def activity_selection(activities, start_times,end_times): 
    result = []
    currStart, currEnd = None, None
    for i in range(len(end_times)):
        if currStart is None:
            result.append(activities[i])
            currStart, currEnd = start_times[i], end_times[i]
        else:
            if start_times[i] >= currEnd:
                start_times = start_times[i]
                currEnd = end_times[i]
                result.append(activities[i])

