# 递归实现
def AckermannRecursion(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return AckermannRecursion(m - 1, 1)
    elif m > 0 and n > 0:
        return AckermannRecursion(m - 1, AckermannRecursion(m, n - 1))


class Ack:
    def __init__(self, m, n):
        self.m = m
        self.n = n


def Ackermann(m, n):
    stack = []
    x = Ack(m, n)
    stack.append(x)
    result = -1
    while len(stack) != 0:
        x = stack.pop()
        if x.m == 0:
            result = x.n + 1
            if len(stack) == 0:
                break
            x = stack.pop()
            x.n = result
            stack.append(x)
        elif x.m > 0 and x.n == 0:
            t = Ack(x.m - 1, 1)
            stack.append(t)
        elif x.m > 0 and x.n > 0:
            t1 = Ack(x.m - 1, -1)
            t2 = Ack(x.m, x.n - 1)
            stack.append(t1)
            stack.append(t2)
    return result


if __name__ == '__main__':
    print(AckermannRecursion(3, 4))
    print(Ackermann(3, 4))
