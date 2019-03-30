li = [1, 2, 3, 4, 5]
for i in li:
    pass
    # print(i)

for i in range(len(li)):
    pass
    # print(li[i])

for i in range(1, 10, 2):
    print(i)

print(li[-1])
print(li[-2])

for i in range(3, -1, -1):
    print(i)

li = []
li.append(1)
li.append(2)
li.append('abc')
li.append(['a', 'b', 'c'])
print(li)

li = [1, 2]
li_2 = [2, 3, 4]
#li.append(li_2)
li.extend(li_2)
# 删除最后元素
li.pop()
li.pop(3)
print(li)
li.sort()
print(li)
