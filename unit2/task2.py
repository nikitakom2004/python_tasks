x=int(input("Введите четырехзначное число"))

x4 = x % 10
x3 = (x//10) % 10
x2 = (x//100) % 10
x1 = (x//1000) % 10

print(x1+x3)
print(x2-x4)