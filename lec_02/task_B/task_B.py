numbers = []
while True:
    num = int(input())
    if num == -2000000000:
        break
    else:
        numbers.append(num)


def get_list_type(numbers: list[int]) -> str:
    last_type = "START"
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            if last_type == "START" or last_type == "CONSTANT":
                last_type = "CONSTANT"
            elif last_type == "ASCENDING" or last_type == "WEAKLY ASCENDING":
                last_type = "WEAKLY ASCENDING"
            elif last_type == "DESCENDING" or last_type == "WEAKLY DESCENDING":
                last_type = "WEAKLY DESCENDING"
            else:
                last_type = "RANDOM"
        elif numbers[i] > numbers[i - 1]:
            if last_type == "START" or last_type == "ASCENDING":
                last_type = "ASCENDING"
            elif last_type == "CONSTANT" or last_type == "WEAKLY ASCENDING":
                last_type = "WEAKLY ASCENDING"
            else:
                last_type = "RANDOM"
        elif numbers[i] < numbers[i - 1]:
            if last_type == "START" or last_type == "DESCENDING":
                last_type = "DESCENDING"
            elif last_type == "CONSTANT" or last_type == "WEAKLY DESCENDING":
                last_type = "WEAKLY DESCENDING"
            else:
                last_type = "RANDOM"
    return last_type


print(get_list_type(numbers=numbers))

# Tests:
assert get_list_type([-530, -530, -530]) == "CONSTANT"
assert get_list_type([-530, -530, 1]) == "WEAKLY ASCENDING"
assert get_list_type([-530, -529, 0]) == "ASCENDING"
assert get_list_type([32, -530, -530]) == "WEAKLY DESCENDING"
assert get_list_type([1244, 124, -5]) == "DESCENDING"
assert get_list_type([-530, -23123, 12321321]) == "RANDOM"
