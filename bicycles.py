#列表
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])      #提取列表内第一个元素
print(bicycles[0].title())      #提取列表内第一个元素并对首字母大写
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print(bicycles[-1].title())     #提取列表内最后一个元素
print('\n')
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)
print('\n------------\n替换列表元素\n\n')
bicycles[0] = '凤凰'
print(bicycles)
print(bicycles[0])
print('\n------------\n增加列表元素\n\n')
bicycles.append('三枪')
print(bicycles)
print('\n------------\n创建空列表并逐渐增加列表元素\n\n')
motorcycles = []
print(motorcycles)
motorcycles.append('hoda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print('\n------------\n在列表指定位置（之前）插入元素\n\n')
print(motorcycles)
motorcycles.insert(0,'dukati')
print(motorcycles)
print(motorcycles[1])       #插入元素后列表更新
motorcycles.insert(-1,'五菱')     #最后一位之前（即倒数第二位）插入元素
print(motorcycles)
print(motorcycles[-2])
print('\n------------\n使用del语句删除列表指定位置元素\n\n')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
print('\n------------\n使用方法pop()弹出列表指定位置元素\n\n')
print(motorcycles)
popped_motorcycle = motorcycles.pop()       #列表末尾元素直接弹出
print(motorcycles)      #打印出剩余元素
print(popped_motorcycle)        #打印出被弹出值
print(motorcycles)
motorcycles.pop(1)      #弹出指定位置元素
print(motorcycles)
print('\n------------\n使用方法remove()弹出列表中指定元素\n\n')
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
too_expensive = 'trek'
bicycles.remove(too_expensive)
print(bicycles)
print(too_expensive)


