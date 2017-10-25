print('-------8.7-----\n')
def make_album(name,album,number = ' '):
    '''创建包含歌手名及专辑的字典'''
    if number != ' ':
        f_name[name] = [album,number]
    else:
        f_name[name] = album       
f_name ={}   
while len(f_name) < 3:
    print('\n(enter "q" to quit!)')
    name = input('name:' )
    if name == 'q':
        break
    album = input('album: ')
    number = input('number: ')
    make_album(name,album,number)    

print(f_name)
