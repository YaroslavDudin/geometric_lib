import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(circle.area(5), 78.53981633974483)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_large(self):
        self.assertAlmostEqual(circle.area(1000000), 3141592653589.793)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            circle.area("5")

    def test_perimeter_normal(self):
        self.assertAlmostEqual(circle.perimeter(5), 31.41592653589793)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_large(self):
        self.assertAlmostEqual(circle.perimeter(1000000), 6283185.307179586)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("5")


class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(rectangle.area(10, 5), 50)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_large(self):
        self.assertEqual(rectangle.area(1000000, 1000000), 1000000000000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-10, 5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("10", 5)

    def test_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_large(self):
        self.assertEqual(rectangle.perimeter(1000000, 1000000), 4000000)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-10, 5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("10", 5)


class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(square.area(4), 16)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_large(self):
        self.assertEqual(square.area(1000000), 1000000000000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            square.area("4")

    def test_perimeter_normal(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_large(self):
        self.assertEqual(square.perimeter(1000000), 4000000)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("4")


class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(triangle.area(10, 5), 25)

    def test_area_zero(self):
        self.assertEqual(triangle.area(10, 0), 0)

    def test_area_large(self):
        self.assertEqual(triangle.area(1000000, 1000000), 500000000000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-10, 5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            triangle.area("10", 5)

    def test_perimeter_normal(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_large(self):
        self.assertEqual(triangle.perimeter(1000000, 1000000, 1000000), 3000000)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("3", 4, 5)


if __name__ == '__main__':
    unittest.main()