p= input('Введите пол:')
v=int(input('Введите возраст:'))
if p=="м" and v>=63 :
    print("пенсия есть")
elif p=="ж" and v>=58:
    print("пенсия есть")
else:
    print("пенсии нет")

