
def display_message(a):
    '''指出在本章中学的是什么'''
    print('本章将学习：' + a)
    
display_message('返回值')

print('-------8.3.1-----\n')

def name(first_name,last_name):
    '''返回完整姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
print(name('jie','chaofan'))

print('-------8.6-----\n')
def city_country(city,country):
    '''返回城市名及所属国家'''
    f_name = '"' + city + ',' + country + '"'
    return f_name
while True :
    print('\n(Enter "q" to quit!)')
    city = input('请输入城市名： ')
    if city  == 'q':
        print('end')
        break
    country = input('请输入国家名： ')
    print(city_country(city,country))

