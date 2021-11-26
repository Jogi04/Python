#!/bin/python


class NewtonVerfahren:
    def __init__(self, start_x=10, iterations=50):
        self.start_x = start_x
        self.iterations = iterations
        self.main_loop()

    def main_loop(self):
        for i in range(self.iterations):
            try:
                new_x = self.return_zero(self.return_m(self.start_x), self.return_b(self.return_y(self.start_x), self.return_m(self.start_x), self.start_x))
            except ZeroDivisionError:
                break
            if self.start_x == new_x:
                break
            self.start_x = new_x
            print(self.start_x)

    def return_y(self, x):
        y = x ** 2 - 5
        return y

    def return_m(self, x):
        f_ = 2 * x
        return f_

    def return_b(self, y, m, x):
        b = y - m * x
        return b

    def return_zero(self, m, b):
        x_zero = -1 * b / m
        return x_zero


if __name__ == '__main__':
    test = NewtonVerfahren(10, 50)
