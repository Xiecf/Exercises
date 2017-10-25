print('\n---5-3------\n')

alien_color = ['green','yellow','red']
print(alien_color)
for a in alien_color:
    if a == 'green':
        x = 5
    if a == 'yellow':
        x = 10
    if a == 'red':
        x = 15
    print('+' + str(x))

age = 60
if age < 2:
    print('You are a baby!')
elif age < 4:
    print('You are a bigbaby!')
elif age < 13:
    print('You are a child!')
elif age < 20:
    print('You are a youth!')
elif age < 65:
    print('You are an adult!')
else:
    print('You are the old!')   
