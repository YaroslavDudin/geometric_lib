import unittest
import math
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(circle.area(5), math.pi * 25)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)


class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(rectangle.area(10, 5), 50)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)


class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(square.area(4), 16)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)


class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(triangle.area(10, 5), 25.0)

    def test_area_zero(self):
        self.assertEqual(triangle.area(10, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()