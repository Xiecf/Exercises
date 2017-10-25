print('\n----5-8-----\n')
a = ['jiechaofan','dingxuejing','admin','jiefeifan']
if a:
    for name in a:
        if name == 'admin':
            print('hello ' + name.upper() + ' morning!')
        else:
            print('hello ' + name.upper())
else:
    print('nothing!')
a = ['jiechaofan','dingxuejing','admin','jiefeifan','DINGXUEJING']
A = ['jiechaofan','dingxuejing','admin','wuzhanwei','fanjiexuan']
print(a)
print(A)
for l in a:
    if l.lower() in A:
        print('请输入其他用户名')
    else:
        print('用户名可用')
a = []
for l in range(1,10):
    a.append(l)
print(a)
for l in a:
    print(str(l) + 'th' + ' ' + str(l))
print('end')
