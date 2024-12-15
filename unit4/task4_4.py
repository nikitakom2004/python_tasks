a = float(input('a='))
b = float(input('b='))

print('1) a + b')
print('2) a – b')
print('3) a * b')
print('4) a / b')
print('5) a % b')

op = int(input('op='))
if op==1:
    print(a+b)
elif op==2:
    print(a-b)
elif op==3:
    print(a*b)
elif op==4 and b!=0:
    print(a/b)
elif op==5:
    print(a%b)
else:
    print('Недопустимая операция')