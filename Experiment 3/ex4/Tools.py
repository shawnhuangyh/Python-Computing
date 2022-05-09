class Customer:
    def __init__(self):
        # self.food = None
        self.food = []

    def placeOrder(self, food, employee):
        self.food.append(employee.takeOrder(food))

    def getOrder(self):
        return self.food


class Employee:
    def takeOrder(self, food):
        return Food(food)


class Food:
    def __init__(self, food=None):
        self.food_name = food

    def __str__(self):
        return self.food_name


class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food=None):
        self.customer.placeOrder(food, self.employee)

    def result(self):
        return self.customer.getOrder()

# if __name__ == '__main__':
#     c = Customer()
#     e = Employee()
#     c.placeOrder("test", e)
#     c.printOrder()
