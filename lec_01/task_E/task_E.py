# For contest without function:
K1, M, K2, P2, N2 = list(map(int, input().split()))
L = (K2 // ((P2 - 1) * M + N2)) # Вычисляем L - кол-во квартир на лестничной площадке
if L < 1:
    print(-1, -1)
else:
    L += 1
    if N2 == P2 == 1:
        P1 = 0
    else:
        P1 = K1 // (M * L) + 1  # Вычисляем P1 - подъезд, в котором находится квартира K1
    if M == 1:
        N1 = M
    elif N2 == P2 == 1:
        N1 = 0
    else:
        N1 = (K1 - (M * L)) // L + 1  # Вычисляем N2 - номер этажа, на котором находится квартира K1
    print(P1, N1)

# In function:
def ambulance(K1: int, M: int, K2: int, P2: int, N2: int) -> tuple:
    L = (K2 // ((P2 - 1) * M + N2)) # Вычисляем L - кол-во квартир на лестничной площадке
    if L < 1:
        return (-1, -1)
    else:
        L += 1
    if N2 == P2 == 1:
        P1 = 0
    else:
        P1 = K1 // (M * L) + 1  # Вычисляем P1 - подъезд, в котором находится квартира K1
    if M == 1:
        N1 = M
    elif N2 == P2 == 1:
        N1 = 0
    else:
        N1 = (K1 - (M * L)) // L + 1  # Вычисляем N2 - номер этажа, на котором находится квартира K1
    return P1, N1


# Tests:
assert ambulance(89, 20, 41, 1, 11) == (2, 3)
assert ambulance(11, 1, 1, 1, 1) == (0, 1)
assert ambulance(3, 2, 2, 2, 1) == (-1, -1)
