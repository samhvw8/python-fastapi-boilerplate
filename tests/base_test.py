from unittest import TestCase

class BaseTest(TestCase):
    def setUp(self):
        print(f"Testing in method: ", self._testMethodName)