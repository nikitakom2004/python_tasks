tc=int(input("Введите температуру в градусах по цельсию:"))

if tc>=30:
    print("За окном жара")
elif tc>=10 and tc<30:
    print("за окном тепло")
elif tc>=0 and tc<10:
    print("За окном холодно")
elif tc<0:
    print("За окном мороз")

