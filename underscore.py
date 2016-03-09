class Underscore(object):
	value = []
	mapped = []
	reduced = []
	rejected = []
	found = 0
	def map(self, arr, function):
		for i in range(0, len(arr)):
			ld = function
			self.mapped.append(ld(arr[i]))
		return self.mapped
	def reduce(self, arr):
		one_digit = 0
		for i in range(0, len(arr)):
			one_digit += arr[i]
		self.reduced.append(one_digit)
		return self.reduced
	def find(self, arr, function, num):
		for x in range(0, len(arr)):
			ld = function(num, arr[x])
			if ld:
				self.found = arr[x]
			else:
				continue
		return True
	def filter(self, arr, function):
		for x in arr:
			data = function
			if data(x):
				self.value.append(x)
		return self.value
	def reject(self, arr, function, num):
		for i in range(0, len(arr)):
			ld = function(num, arr[i])
			if ld:
				continue
			else:
				self.rejected.append(arr[i])
		return self.rejected

# Let's create an instance of our class
# _ = Underscore() # yes we are setting our instance to a variable that is an underscore
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# add2 = _.map([1, 2, 3, 4, 5, 6], lambda x: x + 2)
# should return [2, 4, 6] after code is implemented
# reduction = _.reduce([1, 2, 3, 4, 5, 6])
# found_it = _.find([1, 2, 3, 4, 5, 6], lambda x, num: x == num, 4)
# rejection = _.reject([1, 2, 3, 4, 5, 6], lambda num, x: num == x, 3)

# print(evens)
# print(add2)
# print(reduction)
# print(found_it)
# print(rejection)