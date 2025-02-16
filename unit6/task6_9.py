N=int(input("Введите целое число: "))
for x in range(1,N+1):
    if N%x==0 and x!=1 and x!=N:
        print("Число не является простым")
        break