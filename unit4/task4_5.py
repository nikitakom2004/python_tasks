s=input('Введите символ:')
if s.isdigit():
    print('цифра')
elif s.isalpha():
    print('буква')
elif s==':' or s==',' or s=='.':
    print('Пунктуация')
