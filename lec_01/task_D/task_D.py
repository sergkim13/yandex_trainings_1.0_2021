from typing import Union


# For contest without function:
a = int(input())
b = int(input())
c = int(input())
if a == 0 and b - c ** 2 == 0:
    print('MANY SOLUTIONS')
elif a == 0 or c < 0 or (c ** 2 - b) % a != 0:
    print('NO SOLUTION')
else:
    print(int((c ** 2 - b) / a))


# In function:
def find_sqrt_roots(a: int, b: int, c: int) -> Union[int, str]:
    if a == 0 and b - c ** 2 == 0:
        return 'MANY SOLUTIONS'
    elif a == 0 or c < 0 or (c ** 2 - b) % a != 0:
        return 'NO SOLUTION'
    else:
        return (c ** 2 - b) / a


# Tests:
assert find_sqrt_roots(1, 0, 0) == 0
assert find_sqrt_roots(1, 2, 3) == 7
assert find_sqrt_roots(1, 2, -3) == 'NO SOLUTION'
assert find_sqrt_roots(0, 0, 0) == 'MANY SOLUTIONS'
