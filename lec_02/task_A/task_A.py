# For contest without function:
numbers = list(map(int, input().split()))


# In function:
def is_ascending(items: list[int]) -> str:
    for i in range(1, len(items)):
        if items[i] <= items[i - 1]:
            return 'NO'
    return 'YES'


# Tests:
assert is_ascending([1, 7, 9]) == 'YES'
assert is_ascending([1, 9, 7]) == 'NO'
assert is_ascending([2, 2, 2]) == 'NO'
assert is_ascending([]) == 'NO'
assert is_ascending([1]) == 'NO'
