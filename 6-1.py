print('\n----6-1-----\n')
dingxuejing = {'city':'beijing',
    'first_name':'ding',
    'last_name':'xuejing',
    'age':'18'
        }
print(dingxuejing['city'])
print(dingxuejing['first_name'])
print(dingxuejing['last_name'])

print('\n----6-2-----\n')
number = {'jiechaofan':'12',
    'dingxuejing':'3',
    'wuzhanwei':'8',
    'fanjiexuan':'6'}
love = ['dingxuejing']
print(number)
print(love)
for i in sorted(number):
    print(i + "'s love number is:\n     " + number[i])
    if i in love:
        print('I love you>')

for name,l in number.items():
    print('\nname:' + name + '\n' + 'l   :' + l)

if 'dingxuejing' in number.keys():
    print('ok')
i = number.keys()
print(i)
i = number.values()
print(i)
