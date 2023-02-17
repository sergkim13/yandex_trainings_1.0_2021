n = int(input())
numbers = list(map(int, input().split()))


def symmetric_progression(n: int, numbers: list[int]):

    def is_symmetric(items: list[int]):
        mid = len(items) // 2
        if items[:mid] == items[-1: -mid-1: -1]:
            return True
        return False

    if is_symmetric(numbers):
        return 0

    numbers_copy = numbers[::]
    for i in range(n):
        trailing_nums = numbers_copy[i::-1]
        progression = numbers + trailing_nums
        if is_symmetric(progression):
            M_numbers = " ".join(list(map(str, trailing_nums)))
            return f'{i + 1}\n{M_numbers}'


print(symmetric_progression(n, numbers))


# Tests
assert symmetric_progression(9, [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 0
assert symmetric_progression(5, [1, 2, 1, 2, 2]) == "3\n1 2 1"
assert symmetric_progression(5, [1, 2, 3, 4, 5]) == "4\n4 3 2 1"
assert symmetric_progression(1, [1]) == 0
assert symmetric_progression(2, [1, 2]) == "1\n1"
