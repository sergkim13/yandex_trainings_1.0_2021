# For contest without function:
new_number = input()
number1 = input()
number2 = input()
number3 = input()
result = []
numbers_list = [new_number, number1, number2, number3]
symbols = ['(', ')', '-', '+']
for i in range(len(numbers_list)):
    for symbol in symbols:
        numbers_list[i] = numbers_list[i].replace(symbol, '')
    if len(numbers_list[i]) == 7:
        numbers_list[i] = f'8495{numbers_list[i]}'
    if i > 0:
        if numbers_list[i][1:] == numbers_list[0][1:]:
            result.append('YES')
        else:
            result.append('NO')
print('\n'.join(result))


# In function:
def check_phone_numbers(
    new_number: str,
    number1: str,
    number2: str,
    number3: str,
) -> str:
    result = []
    numbers_list = [new_number, number1, number2, number3]
    symbols = ['(', ')', '-', '+']
    for i in range(len(numbers_list)):
        for symbol in symbols:
            numbers_list[i] = numbers_list[i].replace(symbol, '')
        if len(numbers_list[i]) == 7:
            numbers_list[i] = f'8495{numbers_list[i]}'
        if i > 0:
            if numbers_list[i][1:] == numbers_list[0][1:]:
                result.append('YES')
            else:
                result.append('NO')
    return '\n'.join(result)


# Tests
assert check_phone_numbers(
    '86406361642',
    '83341994118',
    '86406361642',
    '83341994118',
) == ('NO\nYES\nNO')
assert check_phone_numbers(
    '+78047952807',
    '+78047952807',
    '+76147514928',
    '88047952807',
) == ('YES\nNO\nYES')