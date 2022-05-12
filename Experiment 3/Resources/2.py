class Time(object):
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __str__(self):
        return '{:02} : {:02} : {:02}'.format(self.__hour, self.__minute, self.__second)

    def __add__(self, other):
        t = int(self) + int(other)
        if t > 3600:
            t -= 3600 * 24
        return self.__class__(t // 3600, t // 60 % 60, t % 60)

    def __lt__(self, other):
        return int(self) < int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __int__(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    def isafter(self, other):
        return self > other

    def time2int(self):
        return int(self)

    def printtime(self):
        return print(self)

    def increment(self, n):
        if n < 0:
            return
        temp = int(self) + n
        self.__hour = temp // 3600 % 24
        self.__minute = temp // 60 % 60
        self.__second = temp % 60


    def isvalid(self):
        return 0 <= self.__hour <= 23 and 0 <= self.__minute <= 59 and 0 <= self.__second <= 59


t1 = Time(21, 3, 24)
t2 = Time(8, 45, 0)
t3 = Time(1, 59, 10)
t4 = Time(24, 45, 45)

# b
print(t1)
print(t1 + t2)

# c
print(t1.time2int())
print(int(t1))

# d
t1.printtime()

# e
print(t1.isafter(t3))

# f
t1.increment(7202)
print(t1)

# g
print(t1.isvalid())
print(t4.isvalid())
