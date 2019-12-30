import unittest

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.expected = [0,1,1,2,3,5,8,13,21,34]
        self.check = []

        self.expected_square = [0,1,4,9,16,25,36,49,64,81]
        self.expected_triangle = [0,1,3,6,10,15,21,28,36,45]
        self.expected_cube = [0,1,8,27,64,125,216,343,516,729]
        self.check_square = []
        self.check_triangle = []
        self.check_cube = []

        self.check_prime = []
        self.expected_prime = [937,941,947,953,967,971,977,983,991,997]

    def test_fib(self):
        '''checks the first 10 values of the fib.py file to make
        sure that it is giving the expected output'''
        from numseq.fib import fib
        for i in range(10):
            self.check.append(fib(i))
        self.assertEqual(self.check, self.expected)

    def test_geo(self):
        '''checks the first 10 values of the three functions in the geo.py
        against lists of the expected values that come from those'''
        from numseq.geo import *
        for i in range(10):
            self.check_square.append(square(i))
            self.check_triangle.append(triangle(i))
            self.check_cube.append(cube(i))
        self.assertEqual(self.check_square, self.expected_square)
        self.assertEqual(self.check_triangle, self.expected_triangle)
        self.assertEqual(self.check_cube, self.expected_cube)

    def test_prime(self):
        from numseq.prime import *
        prime_list = primes(1000)
        for p in prime_list[-10:]:
            self.check_prime.append(p)
        self.assertEqual(self.check_prime, self.expected_prime)
        self.assertEqual(is_prime(999981), "False")
        self.assertEqual(is_prime(999983), "True")
