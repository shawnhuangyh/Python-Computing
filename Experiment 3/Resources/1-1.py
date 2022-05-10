# 编写 Ackermann 函数的递归实现 Ack（m,n）
def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))

class node:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def __str__(self):
        return '({}, {})'.format(self.m, self.n)
    def __repr__(self):
        return '({}, {})'.format(self.m, self.n)

import copy
# stack
def Ack(m, n):
    res = 0
    stack = []
    x = node(m, n)
    stack.append(x)
    while len(stack) != 0:
        t = copy.deepcopy(stack[-1])
        while t.m > 0 and t.n > 0:
            t.n -= 1
            stack.append(node(t.m, t.n))
            print(stack)

        while t.m > 0 and t.n == 0:
            t = stack.pop()
            print(stack)
            t.m -= 1
            t.n = 1
            stack.append(node(t.m, t.n))
            print(stack)

        while t.m == 0:
            res = t.n + 1
            stack.pop()
            print(stack)
            if len(stack) == 0:
                break
            t = stack.pop()
            print(stack)
            t.m -= 1
            t.n = res
            stack.append(node(t.m, t.n))
            print(stack)
    return res

# m, n = map(int, input().split())
# print(Ackermann(m, n))
print(Ack(3, 4))