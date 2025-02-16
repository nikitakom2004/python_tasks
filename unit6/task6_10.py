n=int(input("Введите целое число: "))
n2=0
l=-1
while n>0:
    m=n%10
    n=n//10
    if m==l:
        print("Одинаковые цифры подряд")
    l=m
