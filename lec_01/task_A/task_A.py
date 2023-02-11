# For contest without function:
temperatures = list(map(int, input().split()))
t_room, t_cond = temperatures[0], temperatures[1]
mode = input()
if mode == 'fan':
    print(t_room)
elif mode == 'heat':
    print(max(t_room, t_cond))
elif mode == 'freeze':
    print(min(t_room, t_cond))
else:
    print(t_cond)


# In function
def freezer(t_room: int, t_cond: int, mode: str) -> int:
    if mode == 'fan':
        return t_room
    elif mode == 'heat':
        return max(t_room, t_cond)
    elif mode == 'freeze':
        return min(t_room, t_cond)
    else:
        return t_cond


# Tests
assert freezer(10, 20, "heat") == 20
assert freezer(10, 20, "fan") == 10
assert freezer(10, 20, "auto") == 20
assert freezer(10, 20, "freeze") == 10
