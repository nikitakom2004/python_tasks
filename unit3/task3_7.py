ta1 = int(input("Введите начало разговора (часы):"))
ta2 = int(input("Введите начало разговора (минуты):"))
ta3 = int(input("Введите начало разговора (секунды):"))

tb1 = int(input("Введите завершение разговора (часы):"))
tb2 = int(input("Введите завершение разговора (минуты):"))
tb3 = int(input("Введите завершение разговора (секунды):"))

ra1 = tb1 - ta1
ra2 = tb2 - ta2
ra3 = tb3 - ta3

rb1 = ra1 * 60
rb3 = ra3 / 60

print((rb1 + rb3 + ra2) * 0.15)
