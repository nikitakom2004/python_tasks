for x in range(100000,1000000):
    s1 = x % 1000
    s2 = x // 1000

    # выделяем разряды трехзначных чисел
    k1 = s1 % 10
    k2 = s2 % 10

    k3 = (s1 // 10) % 10
    k4 = (s2 // 10) % 10

    k5 = s1 // 100
    k6 = s2 // 100

    if (k1 + k3 + k5) == (k2 + k4 + k6):
        print("билет счастливый" ,x)

