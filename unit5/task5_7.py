h=int(input('Введите часы: '))
m=int(input('Введите минуты: '))
if h>=6 and h<12:
    print("доброе утро")
elif h>=12 and h<16:
    print("добрый день")
elif h>=16 and h<21:
    print("добрый вечер")
else:
    print("доброй ночи")
