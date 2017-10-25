squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)
print(squares)
print('\n列表解析\n')
squares = [value**2 for value in range(1,11)]
print(squares)

print('\n练习4-3\n')
numbers = []
for number in range(1,21):
    print(number)
    
numbers = [number for number in range(1,21)]
print(numbers)

numbers = []
for number in range(1,10001):
    print(number)
    numbers.append(number)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = []
for number in range(1,10001,2):
    print(number)
    numbers.append(number)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = []
for number in range(3,31,3):
    print(number)
    numbers.append(number)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print('\n立方')
numbers = []
for number in range(1,10):
    print(number**3)
    numbers.append(number**3)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
number = 1
numbers = []
numbers = [number**3 for number in range(1,10)]
print(numbers)
