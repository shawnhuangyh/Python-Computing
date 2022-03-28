import math

if __name__ == '__main__':
    for i in range(10):
        fracPi = 0
        for k in range(i + 1):
            numerator = math.factorial(4 * k) * (1103 + 26390 * k)
            denominator = math.pow((math.factorial(k)), 4) * math.pow(396, 4 * k)
            fracPi += numerator / denominator
        fracPi *= 2 * math.sqrt(2) / 9801
        Pi = 1 / fracPi
        difference = abs(math.pi - Pi)

        print("\n===============")
        print("Sum {} times:".format(i + 1))
        print("Pi calculation:{:.16f}".format(Pi))
        print("math.pi value:{:.16f}".format(math.pi))
        print("Difference:{:.16f}".format(difference))
