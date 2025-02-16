# Ввод данных
N = int(input("Введите количество кур: "))
M = float(input("Введите стоимость одной курицы: "))
X = int(input("Введите сколько яиц в неделю несёт одна курица: "))
Z = float(input("Введите цену за десяток яиц: ")) * 10
VAT_rate = 0.2 # Ставка НДС

# Расчёт окупаемости
total_cost = N * M # Общая стоимость кур
weekly_eggs = N * X # Общее количество яиц в неделю
daily_eggs = weekly_eggs / 7 # Количество яиц в день
revenue_per_day = daily_eggs * Z # Доход в день
days_to_payback = total_cost / revenue_per_day # Дней до окупаемости

print("С учётом НДС, но без учёта сбора в ПФ, куры окупятся за", days_to_payback, "дней.")