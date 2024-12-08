import decimal

solar_system = {
    'Jupiter':  1898187,
    'Saturn': 568317,
    'Uranus': 86813,
    'Neptune': 102413,
    'Earth': 5972.4,
    'Venus':  4867.5,
    'Mars': 641.71,
    'Mercury':  330.11
}

summ = decimal.Decimal(0)

print(summ)

for p in solar_system:
    summ += decimal.Decimal(solar_system[p])

cr=summ/8
print(cr)
print(summ)

for p in solar_system:
    print(p,'=', decimal.Decimal(solar_system[p])*100/summ, "%")

n = solar_system['Jupiter']/(summ - solar_system['Jupiter'])
print(n)