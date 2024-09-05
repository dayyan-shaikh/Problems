nums = [1,2,3,1]

# approach 1
# num = []
# for i in nums:
#     if i not in num:
#         num.append(i)
# if len(nums) != len(num):
#     print(True)
        

# approach 2
# num = list(set(nums))
# if len(nums) != len(num):
#     print(True)
# else:
#     print(False)