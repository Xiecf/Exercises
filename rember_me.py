print('---10.4.2保存和读取用户生成的数据---')

import json

def get_stored_username():
    '''如果存储了用户名就获取它'''

    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def greet_user():
    user_name = get_stored_username()
    if user_name:
        print('Welcome back, ' + user_name + ' !')
    else:
        username = input('What is your name ? ')
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print('We will rember you when you come back, ' +  username + '!')

greet_user()
