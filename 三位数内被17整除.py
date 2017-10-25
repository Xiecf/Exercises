s = 0
for i in range(1,11):
    s = (s+1000)*(1+0.047)
    print(i,s)

a = 10
b = 40
c = 15
d = []
x = 0
while a*x**2 + b*x + c == 0:
    d.append(x)
    print(x)
