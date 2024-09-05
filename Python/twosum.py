nums = [2,7,8,3,5]
target = 9

# nums = [3,2,4]
# target = 6

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])