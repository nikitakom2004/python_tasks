m = float(input('s='))

t = int(m)
k = int(m % 1 * 1000)
g = int(m * 1000 % 1 * 1000)
print(t, 'тонн', k, 'кг', g, 'гр')