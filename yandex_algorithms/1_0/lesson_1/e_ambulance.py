from math import ceil


def check_room(ap_fl, fl, k2, k):
    return (ap_fl + k) * (fl - 1) < k2 <= (ap_fl + k) * fl


def check_entrance_and_floor(ap_fl, check, n1):
    entrance = ceil(K1 / ap_fl / M)
    if P1 != entrance:
        check = 0
    if n1 != ceil((K1 - (entrance - 1) * ap_fl * M) / ap_fl):
        n1 = 0
    return check, n1


K1, M, K2, P2, N2 = (int(i) for i in input().split())

floor = (N2 + M * (P2 - 1))
apart_floor = ceil(K2 / (N2 + M * (P2 - 1)))
check_P = 1
P1, N1 = 0, 0

if N2 == P2 == 1:
    if K1 <= K2:
        P1, N1 = 1, 1
    elif K1 <= M * K2:
        P1 = 1
    if M == 1:
        N1 = 1
elif not check_room(apart_floor, floor, K2, 0):
    P1, N1 = -1, -1
elif K2 >= (M * (P2 - 1) + N2) and (M >= N2):
    P1 = ceil((K1 / apart_floor) / M)
    N1 = ceil((K1 - (P1 - 1) * apart_floor * M) / apart_floor)
    if check_room(apart_floor, floor, K2, -1) or check_room(apart_floor, floor, K2, 1):
        i = 1
        while check_room(apart_floor, floor, K2, -i):
            check_P, N1 = check_entrance_and_floor(apart_floor - i, check_P, N1)
            i += 1
        j = 1
        while check_room(apart_floor, floor, K2, j):
            check_P, N1 = check_entrance_and_floor(apart_floor + j, check_P, N1)
            j += 1
        if check_P == 0 and K1 <= ((apart_floor - i + 1) * M):
            P1 = 1
        elif check_P == 0:
            P1 = 0
else:
    P1, N1 = -1, -1

print(P1, N1)
