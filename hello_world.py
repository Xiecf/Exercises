name = 'xie chao fan'
print(name.title())    #首字母大写
print(name.upper())    #全部字母大写
print(name.lower())    #全部字母小写
print('\n字符串拼接')    
first_name = 'xie'
last_name = 'chaofan'
full_name = first_name + ' ' + last_name
message = 'hello,' + full_name.title() + '!'
print(message)
print('\n')
favorite_language = ' python '
print(favorite_language.lstrip())   #去除末尾空白
print(favorite_language.rstrip())   #去除首端空白 
print(favorite_language.strip())    #去除首尾两端空白
favorite_language = favorite_language.strip()   #重新定义变量
print(favorite_language)
print('\n')
print ('\txie\n\tchaofan')  #添加制表符和换行符
