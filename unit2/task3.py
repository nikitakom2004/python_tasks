x=int(input("Введите трехзначное число"))

x3 = x % 10
x2 = (x//10) % 10
x1 = (x//100) % 10

print(x1+x3)