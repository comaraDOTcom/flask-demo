# unit test class
import unittest
# according to TDD -> RED-GREEN-BLUE.
# fail our unit test, then implement our business case depending on criteria.
# we fail it at the beginning.
# as a developer (we do so much copy and paste) then by doing RGB, we will be
# sure our methods work
# when they eventually pass.
from fizzbuzz_service import FizzBuzzService


class FizzBuzzServiceTest(unittest.TestCase):
    def test_firsttest(self):
        self.assertEqual('fail', FizzBuzzService.validate(32))

    # implemenent first acceptance criteria
    def test_fizz(self):
        self.assertEqual('Fizz', FizzBuzzService.validate(3))
        self.assertEqual('Fizz', FizzBuzzService.validate(6))

    def test_buzz(self):
        self.assertEqual('Buzz', FizzBuzzService.validate(5))
        self.assertEqual('Buzz', FizzBuzzService.validate(10))

    def test_fizzbuzz(self):
        self.assertEqual('FizzBuzz', FizzBuzzService.validate(45))
        self.assertEqual('FizzBuzz', FizzBuzzService.validate(60))


# this is green phase (passing). this is a good way to start as we are
# iteratively improving our code.

# Blue phase we must now optimise.
# this is working. so if we have error, we will now
