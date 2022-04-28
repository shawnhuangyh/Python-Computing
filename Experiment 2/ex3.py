import random


def sum_same_birthday(student):
    day = [0] * 365
    for i in range(student):
        birthday = random.randint(0, 364)
        if day[birthday] == 0:
            day[birthday] = 1
        else:
            return True
    return False


def get_calculation(m, n):
    q = 0
    for i in range(m):
        if sum_same_birthday(n):
            q += 1
    p = q / m
    return p, q


if __name__ == '__main__':
    m = int(input("Input class numbers(M):"))
    n = int(input("Input student numbers in each class(N):"))
    p, q = get_calculation(m, n)
    print("Q={}".format(q))
    print("P={}".format(p))
