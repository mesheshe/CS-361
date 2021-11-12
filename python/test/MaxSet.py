def decode(nums, memo):
    choice, i = [],len(memo)-1 
    while i >= 0:
        if memo[i] == nums[i-1]:
            choice.insert(0, memo[i])
            return choice
        elif memo[i] == memo[i-1]: # we don't include curr value
            pass 
        else: # we include curr value
            choice.insert(0,memo[i]-memo[i-2])
            i -= 1
        i -= 1
    return choice 


def max_independent_set(nums, memo = None):
    if memo is None:
        memo = [0]*(len(nums)+1)
    for index in range(1, len(memo)):
        if index == 1:
            memo[index] = nums[index-1]
        else:
            memo[index] = max(nums[index-1], nums[index-1] + memo[index - 2], memo[index - 1])
    print(memo, nums)
    return decode(nums, memo)
      
print(max_independent_set([1,0,0,0,0, 100]))
# [7,2,5,20] [-1, -1, 0]