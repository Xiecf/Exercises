print('-------8-1-----\n')
def display_message(a):
    '''指出在本章中学的是什么'''
    print('本章将学习：' + a)
    
display_message('函数')

print('-------8-3-----\n')

def make_shirt(a = 'big',b = 'I love python!'):
    '''制作T恤'''
    print(a + ' is ' + b)
make_shirt(a = '8#',b = 'good')
make_shirt('8#','good')
make_shirt()
make_shirt('mid')
make_shirt(b = 'good')
