print('\n----6-7-----\n')
dingxuejing = {'city':'beijing',
    'first_name':'ding',
    'last_name':'xuejing',
    'age':'18'
        }
fanjiexuan = {'city':'beijing',
    'first_name':'fan',
    'last_name':'jiexuan',
    'age':'27'
        }
jiechaofan = {'city':'tianjin',
    'first_name':'jie',
    'last_name':'chaofan',
    'age':'28'
        }
people = [dingxuejing,fanjiexuan,jiechaofan]
print(people)

print('\n----6-8-----\n')

gege = {'名字':'gege','类型':'猪','主人':'丁雪晶'}
lele = {'名字':'lele','类型':'cat','主人':'范杰轩'}
erduo = {'名字':'erduo','类型':'dog','主人':'解柯心'}
pets = [gege,lele,erduo]
print(pets)
for i in pets:
    print(i)
  
print('\n----6-10-----\n')  
number = {'jiechaofan':['12','15'],
    'dingxuejing':['3','5'],
    'wuzhanwei':'8',
    'fanjiexuan':'6'}
love = ['dingxuejing']
print(number)
for name,lovenumber in sorted(number.items()):
    if len(lovenumber) > 1:
        print(name + '喜欢的数字是:')
        print(lovenumber)
    else:
        print(name + '只喜欢的数字是:')
        print(lovenumber)

