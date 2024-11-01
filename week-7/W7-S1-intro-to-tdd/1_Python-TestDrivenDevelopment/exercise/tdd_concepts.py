import unittest

# Palindrome Check
def isPalindrome(s):
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(isPalindrome("malayalam"))
        self.assertFalse(isPalindrome("tomorrow"))
    pass    

# Alphabet Check
def is_alpha(s):
    return s.isalpha()

class TestAlphabetCheck(unittest.TestCase):
    def test_is_alpha(self):
        self.assertTrue(is_alpha("malayalam"))
        self.assertFalse(is_alpha("test/13"))
    pass

# **Math Operations** - Write tests for basic math functions like multiplication and division.
# Basic Math Operations
def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    pass

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(6, 0), 0)
    pass


#. **Fibonacci Sequence** - Write tests and implement a function to calculate the nth Fibonacci number.

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


# **Anagram Check**
# Anagram Check
def is_anagram(s1, s2):
    return sorted(s1)== sorted(s2)


class TestAnagram(unittest.TestCase):
    def test_is_anagram(self):
# Write failing tests, then implement function and refactor
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("hardest", "easiest"))
        pass

# ----------------------------
# Running the Tests
# ----------------------------
if __name__ == '__main__':
    unittest.main()  # Runs all tests across all classes