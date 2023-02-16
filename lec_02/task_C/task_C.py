n = int(input())
numbers = list(map(int, input().split()))
target = int(input())


def find_closest(n: int, numbers: list[int], target: int) -> int:
    closest = 0
    best_diff = 2000
    for num in numbers:
        diff = abs(target - num)
        if diff <= best_diff:
            best_diff = diff
            closest = num
    return closest


print(find_closest(n, numbers, target))

# Tests
assert find_closest(5, [1, 2, 3, 4, 5], 6) == 5
assert find_closest(5, [5, 4, 3, 2, 1], 3) == 3
assert find_closest(5, [-5, -1000, 0, 0, 0], -6) == -5
assert find_closest(1, [-1000], 1000) == -1000
