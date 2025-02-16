n=int(input("Введите целое число: "))
n2=0

while n>0:
    m=n%10
    n=n//10
    n2=n2*10
    n2=n2+m
print(n2)

