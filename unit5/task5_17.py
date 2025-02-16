import random

balance = 5000  # начальный баланс

while balance > 0:
    # генерация случайной комбинации
    combo = [random.randint(0, 7) for _ in range(3)]
    current_combo = ''.join(str(x) for x in combo)
    print('текущая комбинация:', current_combo)

    # проверка на призовую или штрафную комбинацию
    if current_combo == '666':
        print('штрафная комбинация')
        balance -= 1000
    elif current_combo == '777':
        print('Джекпот!')
        break
    elif current_combo in ['000', '111', '222', '333', '444', '555']:
        print('начисление выигрыша')
        balance += 300
    elif current_combo.startswith('5') or current_combo.startswith('7'):
        print('начисление выигрыша')
        balance += 100
    else:
        # нейтральная комбинация
        balance -= 500

    input(f"Баланс {balance} Нажмите enter клавишу чтобы продолжить")

print("Игра окончена!")

