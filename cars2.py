cars = ['bmw','audi','toyota','subaru']
for car in cars:
    if car == 'bmw':
            print(car.upper())
    else:
        print(car.title())

car = 'bwm'
print(car == 'bwm')
print(car == 'BWM')
print(car.upper() == 'BWM')
print(car == 'audi')
a = 'xiechaofan'
b = 'Xiechaofan'
c = 'gaojinlei'
d = ['xiechaofan','Xiechaofan','gaojinlei']
for i in d:
    if i == b:
        print('相同')
    else:
        print('不同')    

for i in d:
    if i == b.lower():
        print('相同')
    else:
        print('不同')    
        
numbers = [1,2,3,4,5]
for number in numbers:
    if number == 3:
        print(str(number) + '=' + '3')
    if number < 3:
        print(str(number) + '<' + '3')
    if number > 3:
        print(str(number) + '>' + '3') 

