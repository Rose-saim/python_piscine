class calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, object):
        self.numbers = [x + object for x in self.numbers]
        print(self.numbers)

    def __sub__(self, object):
        self.numbers = [x - object for x in self.numbers]
        print(self.numbers)

    def __mul__(self, object):
        self.numbers = [x * object for x in self.numbers]
        print(self.numbers)

    def __truediv__(self, object):
        if object == 0:
            raise ValueError("Division by zero is not allowed.")
        self.numbers = [x / object for x in self.numbers]
        print(self.numbers)
