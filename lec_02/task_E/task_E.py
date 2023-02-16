n = int(input())
lengths = list(map(int, input().split()))


def find_position(n: int, lengths: list[int]) -> int:
    sorted_lengths = sorted(lengths, reverse=True)
    answer = 0
    winner_index = 0
    best_length = min(lengths)
    # Определяем индекс победителя
    for i in range(1, n):
        if lengths[i] > lengths[winner_index]:
            winner_index = i
    if winner_index >= n - 2:
        return answer
    # Определяем наилучшую возможную длину броска Василия
    for i in range(winner_index + 1, n - 1):
        if str(lengths[i]).endswith('5') and lengths[i] > lengths[i + 1]:
            best_length = max(best_length, lengths[i])
    # Если лучшая длина броска изменилась, то определяем позицию Василия
    # в отсортированном по убыванию списке
    if best_length > min(lengths):
        answer = sorted_lengths.index(best_length) + 1
    return answer


print(find_position(n, lengths))

# Tests
assert find_position(7, [10, 20, 15, 10, 30, 5, 1]) == 6
assert find_position(3, [15, 15, 10]) == 1
assert find_position(3, [10, 15, 20]) == 0
assert find_position(3, [10, 120, 20]) == 0
assert find_position(9, [10, 10, 10, 8, 8, 5, 6, 5, 2]) == 7
assert find_position(9, [10, 999, 10, 90, 8, 100, 6, 5, 2]) == 8
assert find_position(4, [10, 999, 15, 3]) == 2
