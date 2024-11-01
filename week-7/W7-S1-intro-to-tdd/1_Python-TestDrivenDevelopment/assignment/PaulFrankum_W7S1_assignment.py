#start writing code from here.
import unittest

# **Factorial Calculation**: `factorial(n)` should compute the factorial of a non-negative integer.
def Factorial(a):
    fact = 1
    for num in range(2, a + 1):
        fact *= num
    return fact

class TestFactorialOperations(unittest.TestCase):
    def test_Factorial(self):
        self.assertEqual(Factorial(5), 120)
        self.assertEqual(Factorial(10), 3628800)
        self.assertEqual(Factorial(40), 815915283247897734345611269596115894272000000000)
    pass
# **GCD Calculation**: `gcd(a, b)` should compute the greatest common divisor of two integers.
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

class TestgcdOperations(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(13, 4), 1)
        self.assertEqual(gcd(43, 24), 1)
        self.assertEqual(gcd(14, 28), 14)
    pass
# **Power Calculation**: `power(base, exponent)` should calculate the base raised to the exponent.
def power(a,b):
    return a**b

class TestpowerOperations(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)
        self.assertEqual(power(4, 4), 256)
        self.assertEqual(power(2, 4), 16)
    pass

# **Sorted List Check**: `is_sorted(lst)` should return `True` if a list is sorted, otherwise `False`.
def is_sorted(list):

    if list == sorted(list):
        return True
    else:
        return False
    
class Testis_sortedOperations(unittest.TestCase):
    def test_is_sorted(self):
        self.assertTrue(is_sorted(['BMW','Ford', 'Volvo']))
        self.assertFalse(is_sorted(['Ford', 'BMW', 'Volvo']))
    pass

# **Nth Fibonacci Number**: `fibonacci(n)` should return the nth Fibonacci number.
def fibonacci(n):
    # Program to display the Fibonacci sequence up to n-th term
     # first two terms
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(6) == 8
        pass

# **Matrix Addition**: `matrix_addition(matrix1, matrix2)` should add two matrices (2D lists) of the same dimensions.
def matrix(x, y, result):
# iterate through rows
    for i in range(len(x)):
        # iterate through columns
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    return result

class TestmatrixOperations(unittest.TestCase):
    def test_matrix(self):
        self.assertEqual(matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]), [[10,10,10], [10,10,10], [10,10,10]])
    pass


# **Area of Rectangle**: `area_rectangle(length, width)` should calculate the area of a rectangle.
def rectangle(a,b):
    return a*b

class TestrectangleOperations(unittest.TestCase):
    def test_rectangle(self):
        self.assertEqual(rectangle(3, 4), 12)
        self.assertEqual(rectangle(9, 8), 72)
        self.assertEqual(rectangle(1, 9), 9)
    pass


# **Area of Circle**: `area_circle(radius)` should calculate the area of a circle.
def pi(a):
    return a*3.1415927

class TestpiOperations(unittest.TestCase):
    def test_pi(self):
        self.assertEqual(pi(3), 9.4247781)
        self.assertEqual(pi(4), 12.5663708)
        self.assertEqual(pi(5), 15.7079635)
    pass

# **Perfect Square Check**: `is_perfect_square(n)` should return `True` if `n` is a perfect square, otherwise `False`.
def square(a):
    return a*a

class TestsquareOperations(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)
        self.assertEqual(square(5), 25)
    pass

# ----------------------------
# Running the Tests
# ----------------------------
if __name__ == '__main__':
    unittest.main()  # Runs all tests across all classes