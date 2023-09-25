import math
import unittest
from task_1 import Circle, Triangle


class TestCircle(unittest.TestCase):

    def test_circle_creation(self):
        self.assertRaises(Exception, Circle, -1)
        self.assertRaises(Exception, Circle, 0)

    def test_property_changing(self):
        circle = Circle(1)
        self.assertRaises(Exception, circle.radius, -1)
        self.assertRaises(Exception, circle.radius, 0)
        self.assertEqual(1, circle.radius)

    def test_square_calculation(self):
        circle = Circle(1)
        self.assertEqual(math.pi, circle.calculate_square())


class TestTriangle(unittest.TestCase):

    def test_triangle_creation(self):
        self.assertRaises(Exception, Triangle, 0, 1, 1)
        self.assertRaises(Exception, Triangle, -1, 1, 1)
        self.assertRaises(Exception, Triangle, 2, 1, 3)

    def test_property_changing(self):
        triangle = Triangle(3, 4, 5)

        for i in [-1, 0, 1]:
            self.assertRaises(Exception, triangle.a, i)
            self.assertRaises(Exception, triangle.b, i)
            self.assertRaises(Exception, triangle.c, i)

    def test_triangle_type_detection(self):
        triangle = Triangle(1, 1, 1)
        self.assertEqual('Standard triangle', triangle.triangle_type())
        triangle = Triangle(3, 4, 5)
        self.assertEqual('Rectangular triangle', triangle.triangle_type())

    def test_triangle_square_calculation(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(6, triangle.calculate_square())


if __name__ == "__main__":
    unittest.main()
