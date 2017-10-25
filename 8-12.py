print('-----8-12-----\n')
def food(*f_material):
    print(f_material)
food('baicai')
food('baicai','hotdog')
food('baicai','hotdog','salt')

print('-----8-13-----\n')
def build_profile(first,last,**user_info):
    a = {}
    a['first_name'] = first
    a['last_name'] = last
    for b,c in user_info.items():
        a[b] = c
    return a

x = build_profile('jie','chaofan',city='beijing',country='china')
print(x)

print('-----8-14-----\n')
def make_car(
        制造商,
        型号,
        **x):
    a = {}
    a['制造商'] = 制造商
    a['型号'] = 型号
    for b,c in x.items():
        a[b] = c
    return a
    
car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)
