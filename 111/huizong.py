d = 'yes'  
zidian = {}
zhuzidian = {}

while d == 'yes' :
    
    #取得用户输入的数据
    a = input('请输入名字：')
    b = input('请输入年龄：')
    c = input('请输入性别：')
 
    #将数据转化为字典
    zidian['年龄'] = b
    zidian['性别'] = c

    #将字典传入主字典
    zhuzidian[a] = zidian
    zidian = {} #重置字典 
    
    d = input('是否继续添加名字（yes or no）：')

#将主字典存入文件
print(zhuzidian)

#filename = 'name_dict.txt'

#with open(filename,'w') as file_object:
    
#    for key in zhuzidian:
#        file_object.write(key)

