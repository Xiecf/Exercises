print('\n-----7.3------\n')
a = ['1','2','3']
b = []
while a:
    c = a.pop()
    b.append(c)
    print(b)

b.append('1')
print(b)
while '1' in b:
    b.remove('1')
    print(b)

d = {}
e = True
while e:
    name = str(input('What is your name? '))
    age = int(input('How old are you? '))
    d[name] = age
    
    f = str(input('another?'))
    if f =='no':
        e = False
print(d)
