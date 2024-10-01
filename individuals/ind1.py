# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поле first — дробное положительное число, катет а прямоугольного треуголь ника; поле
# second — дробное положительное число, катет прямоугольного треугольника. Реализовать
# метод hypotenuse() — вычисление гипотенузы.

import math


class RightTriangle:
    def __init__(self, first, second):
        if not isinstance(first, (int, float)) or not isinstance(
            second, (int, float)
        ):
            raise ValueError("The first and second inputs must be numbers")
        if first <= 0 or second <= 0:
            raise ValueError("The numbers must be > 0")
        self.first = first
        self.second = second

    def read(self):
        try:
            first = float(input("Enter first value > 0: "))
            second = float(input("Enter second value > 0: "))
            if first <= 0 or second <= 0:
                raise ValueError("The numbers must be > 0")
            self.first = first
            self.second = second
        except ValueError as error:
            print(error)
            self.read()

    def display(self):
        print(f"The catheter a={self.first}, the catheter b={self.second}")

    def hypotenuse(self):
        return math.sqrt(self.first**2 + self.second**2)


def make_right_triangle(first, second):
    try:
        return RightTriangle(first, second)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    triangle1 = make_right_triangle(3, 4)
    triangle1.display()
    print(triangle1.hypotenuse())

    triangle2 = make_right_triangle(3, 4)
    triangle2.read()
    triangle2.display()
    print(triangle2.hypotenuse())
