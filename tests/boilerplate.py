from src.matrix import Matrix


class Boilerplate:
	def __init__(self):
		self.m1 = Matrix([[1, 123124142, 143, 46545],
		                  [5, 6, 7, 8],
		                  [10, 1211, 12, 1321, 146436]])
		# mag=6 c=5 r=3
		self.m2 = Matrix([[80, 8, 8, 8],
		                  [8, 8000, 80000, 8, 2],
		                  [8, 8, 8, 800000]])
		# mag=1 c=4 r=3
		self.m3 = Matrix([[8, 8, 8, 8],
		                  [8, 8, 8, 8],
		                  [8, 8, 8, 8]])

		# mag=5 c=4 r=3
		self.m4 = Matrix([[8, 8, 8, 8],
		                  [8, 8, 8, 8],
		                  [8, 8, 8, 8],
		                  [80, 800, 8000, 80000]])

		self.m5 = Matrix([[1, 123124142, 143, 46545, 5, 1, 2],
		                  [5, 6, 7, 8],
		                  [10, 1211, 12, 1321, 146436]])

		self.m = Matrix([['A', 'B', 'C', 'D', None],
		                 ['E', 'F', 'G', 'H', 'I'],
		                 ['J', 'K', 'L', 'M', None]])

	def basic_test(self, res, expected, res_type):
		self.is_equal(res, expected)

		self.is_instance(res, res_type)

		# if res_type is list:
		# 	for v in res:
		# 		self.is_instance(v, Vector)

		# if index_type_pairs is not None:
	# 	for k, v in index_type_pairs.items():
	# 		self.is_instance(res[k], v)

	@staticmethod
	def is_equal(x, y):
		assert x == y

	@staticmethod
	def not_is_equal(x, y):
		assert x != y

	@staticmethod
	def is_instance(x, t):
		assert x is None if t is None else isinstance(x, t)

	@staticmethod
	def not_is_instance(x, t):
		assert x is not None if t is None else not isinstance(x, t)

	@staticmethod
	def is_a(x, y):
		assert x is y

	@staticmethod
	def not_is_a(x, y):
		assert x is not y
