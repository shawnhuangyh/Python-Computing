import random


def remove_repetition(x):
    element = set()
    if isinstance(x, list):
        x = x[::-1]
        for i in range(len(x) - 1, -1, -1):
            if x[i] in element:
                del (x[i])
            else:
                element.add(x[i])
        return x[::-1]
    elif isinstance(x, dict):
        for i in range(len(x)):
            if x[i] in element:
                x.pop(i)
            else:
                element.add(x[i])
        return x


if __name__ == '__main__':
    # List
    print("List:")
    x = [random.randint(0, 50) for i in range(100)]
    print("Before removal:")
    print(x)
    print("After removal:")
    y = remove_repetition(x)
    print(y)
    # Dictionary
    print("Dictionary:")
    x = {i: random.randint(0, 50) for i in range(100)}
    print("Before removal:")
    print(x)
    print("After removal:")
    y = remove_repetition(x)
    print(y)
