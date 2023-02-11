# For contest without function:
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')


# In function
def triangle(a: int, b: int, c: int) -> str:
    if a + b > c and a + c > b and b + c > a:
        return 'YES'
    return 'NO'


# Tests
assert triangle(3, 4, 5) == 'YES'
assert triangle(3, 5, 4) == 'YES'
assert triangle(4, 5, 3) == 'YES'
assert triangle(12, 5, 3) == 'NO'
