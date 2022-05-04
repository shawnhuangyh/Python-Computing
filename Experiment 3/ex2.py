class Time:
    def __init__(self, h=0, m=0, s=0):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __str__(self):
        return str(self.__hour).zfill(2) + ":" + str(self.__minute).zfill(2) + ":" + str(self.__second).zfill(2)

    def __add__(self, x):
        if isinstance(x, Time):
            if self.isvalid() == False or x.isvalid() == False:
                return
            a = Time()
            # Add second
            a.__second += self.__second + x.__second
            if a.__second >= 60:
                a.__second -= 60
                a.__minute += 1
            # Add minute
            a.__minute += self.__minute + x.__minute
            if a.__minute >= 60:
                a.__minute -= 60
                a.__hour += 1
            # Add hour
            a.__hour += self.__hour + x.__hour
            if a.__hour >= 24:
                a.__hour -= 24
            return a

    def time2int(self):
        minute = self.__hour * 60 + self.__minute
        second = minute * 60 + self.__second
        return second

    def isafter(self, x):
        if isinstance(x, Time):
            if self.isvalid() == False or x.isvalid() == False:
                return
            if self.__hour > x.__hour:
                return 1
            elif self.__hour == x.__hour:
                if self.__minute > x.__minute:
                    return 1
                elif self.__minute == x.__minute:
                    if self.__second > x.__second:
                        return 1
                    elif self.__second == x.__second:
                        return 0
                    else:
                        return -1
                else:
                    return -1
            else:
                return -1

    def increment(self, n):
        if isinstance(n, int) and n > 0:
            if self.isvalid() == False:
                return
            second = n % 60
            minute = (n // 60) % 60
            hour = n // 3600
            temp = Time(hour, minute, second)
            temp += self
            return temp

    def isvalid(self):
        if self.__hour < 0 or self.__hour >= 24:
            return False
        else:
            if self.__minute < 0 or self.__minute >= 60:
                return False
            else:
                if self.__second < 0 or self.__second >= 60:
                    return False
                else:
                    return True


if __name__ == '__main__':
    # 创建时间实例
    a = Time(12, 22, 30)
    b = Time(11, 50, 10)
    # 输出时间
    print("输出时间：", end="")
    print(a)
    # 时间相加
    print("时间相加：", end="")
    c = a + b
    print(c)
    # 时间转化为秒
    print("时间转换为秒：", end="")
    print(a, ":", a.time2int())
    # 判断时间先后
    print("判断时间先后：", end="")
    print("A和B时间相比：", a.isafter(b))
    # 经过n秒
    print("时间经过n秒：", end="")
    print(a, "经过250秒为：", a.increment(250))
    # 判断时间合法
    print("时间合法：")
    print(a.isvalid())
    c = Time(25, 22, 67)
    print(c.isvalid())
