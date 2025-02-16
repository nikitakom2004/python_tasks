import random
n=int(input("Введите целое число: "))
for p in range(0,100):
    r = random.randint(0, 1001)
    print(r)
    if r==n:
        print("угадали число")
        break
    else:
        print("не угадали число")
