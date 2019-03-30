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


# lamda
#le = [[5, 2], [3, 8], [2, 11], [7, 6]]
#le.sort(lambda x: x[0])
#print(le)


tp = (1, 2, 3)
try:
    tp[0] = 100
except Exception as e:
    print(e)

s = set([1, 2, 3, 4, 4, 4])
print(s)
s = set((2, 3, 3, 4, 2, 2))
print(s)

# dict
di = {'ki': 'v1', 'k2': 'v2'}
di['k3'] = 'v3'
di['k4'] = 'v4'
for k in di:
    print(di[k])

for k, v in di.items():
    print(k, v)

li = [1, 2, 3, 4, 5]
li_0_2 = li[0:3]
print(li_0_2)

li_last_3 = li[-1:  -4: -1]
print(li_last_3)
# 反转数组
print(li[::-1])