import random

r1=random.randint(1,42)
r2=random.randint(1,42)
r3=random.randint(1,42)
r4=random.randint(1,42)
r5=random.randint(1,42)

y1=int(input("Введите первое число:"))
y2=int(input("Введите второе число:"))
y3=int(input("Введите третье число:"))
y4=int(input("Введите четвертое число:"))
y5=int(input("Введите пятое число:"))

c=0 # счетчик угаданных чисел

# проверяем что введенные числа попали в диапазон загаданных (случайных) чисел
if y1 in [r1,r2,r3,r4,r5] :
    print("первое число угадано")
    c=c+1 # увеличиваем счетчик угаданных чисел
if y2 in [r1,r2,r3,r4,r5] :
    print("второе число угадано")
    c=c+1 # увеличиваем счетчик угаданных чисел
if y3 in [r1,r2,r3,r4,r5] :
    print("третье число угадано")
    c=c+1 # увеличиваем счетчик угаданных чисел
if y4 in [r1,r2,r3,r4,r5] :
    print("четвертое число угадано")
    c=c+1 # увеличиваем счетчик угаданных чисел
if y5 in [r1,r2,r3,r4,r5] :
    print("пятое число угадано")
    c=c+1 # увеличиваем счетчик угаданных чисел

print(f"Вы угадали {c} чисел")
if c==3:
    print("300  рублей")
elif c==4:
    print("4000 рублей")
elif c==5:
    print("5000 рублей")