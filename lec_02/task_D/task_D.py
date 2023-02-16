numbers = list(map(int, input().split()))


def find_greater_than_neighbours(numbers: list[int]) -> int:
    answer = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            answer += 1
    return answer


print(find_greater_than_neighbours(numbers))

# Tests
assert find_greater_than_neighbours([1, 2, 3, 4, 5]) == 0
assert find_greater_than_neighbours([5, 4, 3, 2, 1]) == 0
assert find_greater_than_neighbours([1, 5, 1, 5, 1]) == 2
