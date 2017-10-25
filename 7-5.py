print('\n-----7-5----\n')
price = ''
active = True
while active :
    price = input('Hou old are you? ')
    if  price == 'quit' :
            break
    else:
        if int(price) == 0 :
            actrve = False

        elif  int(price) < 3 :
            print('fee')
        elif int(price) < 12 :
            print('10')
        else:
            print('15')
