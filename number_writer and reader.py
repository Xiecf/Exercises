print('---使用json.dump()存储数字列表---\n')

import  json

number = [1,3,5,7,9]
filename = 'number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)


print('---使用json.load()读取列表到内存中---\n')

with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)
