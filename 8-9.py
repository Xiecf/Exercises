print('-----8-9-----\n')
def show_magicians(names):
    for name in names:
        print(name)
def make_great(greats):
    for a in range(len(greats)):
        greats[a] = 'the great ' + greats[a]
    return greats

i = ['jiechaofsn','dingxuejing','fanjiexuan']
o = i[:]
show_magicians(i)
make_great(o)
show_magicians(o)
