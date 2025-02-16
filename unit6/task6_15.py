def convert_to(number, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result

print(convert_to(123,2))
print(convert_to(123,8))
print(convert_to(123,16))