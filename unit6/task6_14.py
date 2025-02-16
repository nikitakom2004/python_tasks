v=0
for x in range(10000000,100000000):
    n=x
    l=-1
    usl=True
    while n > 0:
        m = n % 10
        n = n // 10
        if m == l:
            usl=False
            break
    if usl == True:
        if x%12345==0:
            print("число найдено",x)
            v=v+1
print("количество найденных чисел=",v)