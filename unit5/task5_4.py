h= int(input('Введите часы:'))
m= int(input('Введите минуты:'))
s= int(input('Введите секунды:'))
if h>=0 and h<=23:
    print("часы корректны")
else:
    print("часы некорректны")
if m>=0 and m<=59:
    print("минуты корректны")
else:
    print("минуты некорректны")
if s>=0 and s<=59:
    print("секунды корректны")
else:
    print("секунды некорректны")
