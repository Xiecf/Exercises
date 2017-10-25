a = []
a.append('fanjiexuan')
a.append('wuzhanwei')
a.append('dingxuejing')
print(a)
a.sort()
print(a)
for friend in a:
	print(friend.title() + ',You are my friend.')
print('They are my frienfs.')


print('\n---4.3.1-----------\n')
sqares = []
for value in range(1,11,2):
	sqares.append(value**2)
	print(value)
print(sqares)
sqares = [value*2 for value in range(1,11,2)]
print(sqares)

print('\n---4.3-----------\n')
for i in range(1,21):
	print(i)

print('\n---4.4-----------\n')
y = [x for x in range(1,1000001)]
#print(y)

print('\n---4.5-----------\n')
print(min(y))
print(max(y))
print(sum(y))

print('\n---4.6-----------\n')
for x in range(1,21,2):
	print(x)

print('\n---4.7-----------\n')
z = [x for x in range(3,31,3)]
print(z)
for a in z:
	print(a)

print('\n---4.8-----------\n')
z = [x**3 for x in range(1,11)]
print(z)
for a in z:
	print(a)

print('\n---4.8-----------\n')
z = [x**3 for x in range(1,11)]
print(z)
print(z[:3])
for t in range(2,10):
	for o in z[:t]:
		print(o)

print('\n---复制列表-----------\n')

z = [x for x in range(0,11)]
print(z)
x = z#列表无法赋值
print(x)
z.append('x')
print(z)
print(x)
del z[-1]
x = z[:]
print(z)
print(x)
z.append('x')
print(z)
print(x)

