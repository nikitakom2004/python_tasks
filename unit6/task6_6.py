n=int(input("Введите целое число: "))
l=0
s=0
while n>0:
    l=l+1
    m=n%10
    s=s+m
    n=n//10
    print(m,n)
print(l)
print(s)