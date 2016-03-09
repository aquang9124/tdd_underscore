import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
	def setUp(self):
		# create an instance of the Underscore module we created
		self._ = Underscore()
		# initialize a list to run our tests on
		self.test_list = [1, 2, 3, 4, 5]
	def testMap(self):
		return self.assertIsInstance(self._.map(self.test_list, lambda x: x + 2), list)
	def testReduce(self):
		return self.assertEqual(1, len(self._.reduce(self.test_list)))
	def testFind(self):
		return self.assertEqual(True, self._.find(self.test_list, lambda x, num: x == num, 4))
	def testFilter(self):
		return self.assertIsInstance(self._.filter(self.test_list, lambda x: x % 2 == 0), list)
	def testReject(self):
		return self.assertIsInstance(self._.reject(self.test_list, lambda num, x: num == x, 3), list)

if __name__ == "__main__":
	unittest.main()