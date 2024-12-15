number1 = int(input('n1='))
number2 = int(input('n2='))
number3 = int(input('n3='))

m=0

if number1<=number2:
    m=number1
else:
    m=number2

if m> number3:
    m=number3

print(m)