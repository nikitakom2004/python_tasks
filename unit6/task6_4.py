tc=int(input("Введите начальная температуру по цельсию: "))
tf=int(input("Введите  конечную температуру по цельсию: "))
for c in range(tc,tf+1):
    print(c)
    f=1.8*c+32
    print(f)