#写入文件
file_path = r'C:\Documents and Settings\Administrator\桌面\Python_work\text_files\name.txt'
with open(file_path,'w') as name:
    x = True
    while x :
        a = input('name or q :\n')
        if a == 'q':
            break
        else:
            print('hello ' + a + ' !')
            name.write(a + '\n')
with open(file_path) as name:  
    print(name.read())
