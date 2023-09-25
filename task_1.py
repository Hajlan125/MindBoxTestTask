import math
import sys
from abc import ABC, abstractmethod


class ShapeInterface(ABC):
    @abstractmethod
    def calculate_square(self):
        pass

    @abstractmethod
    def _is_existing(self):
        pass


class Circle(ShapeInterface):
    def __init__(self, radius):
        self._radius = radius
        self._is_existing()

    def _is_existing(self):
        if self._radius <= 0:
            raise Exception('This circle can not exist')

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._is_existing()

    def calculate_square(self):
        return math.pi * self.radius ** 2


class Triangle(ShapeInterface):
    def __init__(self, a, b, c):
        self._a, self._b, self._c = a, b, c
        self._is_existing()

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a
        self._is_existing()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b
        self._is_existing()

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c
        self._is_existing()

    def _is_existing(self):
        if self._a <= 0 or self._b <= 0 or self._c <= 0:
            raise Exception("This triangle can not exist")
        if self._a + self._b <= self._c or self._a + self._c <= self._b or self._b + self._c <= self._a:
            raise Exception("This triangle can not exist")

    def triangle_type(self):
        arr = [i ** 2 for i in sorted([self._a, self._b, self._c], reverse=True)]
        if arr[0] == sum(arr[1:]):
            return 'Rectangular triangle'
        else:
            return 'Standard triangle'

    def calculate_square(self):
        half_perimeter = (self._a + self._b + self._c) / 2

        heron_formula = (half_perimeter * (half_perimeter - self._a) * (half_perimeter - self._b)
                         * (half_perimeter - self._c))
        return math.sqrt(heron_formula)


class Calculator:

    def start(self):
        choices = {
            'круг': self.circle_info_output,
            'треугольник': self.triangle_info_output,
            'стоп': self.stop
        }
        print(f'Введите необходимую фигуру из списка: {list(choices.keys())} ')
        key = input()

        if key.lower() not in [x.lower() for x in list(choices.keys())]:
            print('Неправильный ввод')

        else:
            choices[key.lower()]()
        print()

    @staticmethod
    def circle_info_output():
        radius = input('Введите радиус: ')
        try:
            circle = Circle(int(radius))
            print(f'Площадь окружности = {circle.calculate_square()}')
        except Exception as e:
            print(e)

    @staticmethod
    def triangle_info_output():
        try:
            a = int(input('Введите сторону а: '))
            b = int(input('Введите сторону b: '))
            c = int(input('Введите сторону c: '))
            triangle = Triangle(a, b, c)
            print(f'Тип треугольника - {triangle.triangle_type()} \n'
                  f'Площадь треугольника = {triangle.calculate_square()}')
        except Exception as e:
            print(e)

    @staticmethod
    def stop():
        sys.exit()


if __name__ == "__main__":
    # circle1 = Circle(1)
    # print(circle1.calculate_square())
    #
    # tri1 = Triangle(1, 1, 1)
    # print(tri1.calculate_square())
    # print(tri1.triangle_type())

    calc = Calculator()
    while True:
        calc.start()
