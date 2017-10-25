print('\n------7-8-----\n')
sandwich_orders = ['a','b','c']
finished_sandwiches = []
while sandwich_orders:
    print('I made your tuna sandwich.')
    x = sandwich_orders.pop()
    finished_sandwiches.append(x)
print(finished_sandwiches)

print('\n------7-9-----\n')
for a in range(3):
    sandwich_orders.append('a')
    
print(sandwich_orders)

print('end')
while sandwich_orders:
    sandwich_orders.remove('a')
print(sandwich_orders)

print('\n------7-10-----\n')
a = {}
f = True
while f:
    name = str(input('What is youor name? '))
    place = str(input('If you could visit one place in the would,where would you go? '))
    a[name] = place
    b = str(input('Go on?(yes/no)'))
    if b == 'no':
        f = False
print(a)
for g,h in a.items():
    print(g + ' will go ' + h + '.')
    
