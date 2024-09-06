s = "leetcode"
dict = {}

for item in s:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)
c=1
for index,char in enumerate(s):
    if dict[char] ==c:
        print(index)
        break
else:
    print("-1")
    