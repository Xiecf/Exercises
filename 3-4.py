yaoqing = []
print(yaoqing)
#增加元素
yaoqing.append('dingxuejing')
print(yaoqing)
yaoqing.append('fanjiexuan')
yaoqing.append('jiechaofan')
print(yaoqing)
print(len(yaoqing))
print(yaoqing[-1])
yaoqing[-1] = 'jiefeifan'
print(yaoqing)
yaoqing.insert(0,'wuzhanwei')
print(yaoqing)
del yaoqing[0]
print(yaoqing)
yaoqing.remove('dingxuejing')
print(yaoqing)
yaoqing.append('apple')
yaoqing.sort()
print(yaoqing)
yaoqing.sort(reverse=True)
print(yaoqing)
