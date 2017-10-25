file_path = r'C:\Documents and Settings\Administrator\桌面\Python_work\text_files\name.txt'
with open(file_path) as name:
    a = name.read()
    print(a.rstrip())
    
print(a.rstrip())

with open(file_path) as name:
    print(name.read())
    
#逐行读取
with open(file_path) as name:
    for line in name:
        print(line.rstrip())
    
with open(file_path) as name:
    lines = name.readlines()
    print(lines)
for line in lines:
    print(line.rstrip())

