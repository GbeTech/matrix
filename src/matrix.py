from typing import List, Union
from helpers import strhelp


# from .utils import transform


# TODO: Custom index titles
# TODO: Check unequal col/row lengths cases

class Vector:
	def __init__(self, value=None):
		self.value = value if value is not None else []

	def __setitem__(self, key, value):
		print('set item!')

	def __getitem__(self, item):
		ret = None

		if isinstance(item, slice):

			# If item is [:]
			if all(sl is None for sl in (item.start, item.stop, item.step)):
				raise NotImplementedError("got [:] for Vector")

			# If item is [:n]
			elif item.start is None:
				ret = self.value[item]
				ret = Matrix.remove_redundant_nesting(ret)
			else:

				ret = self.value[item]

		else:
			ret = self.value[item]

		return ret

	# def __iter__(self):
	# 	yield self.value

	def __eq__(self, other):
		return self.value == other

	def __str__(self):
		if any(isinstance(i, Vector) for i in self.value) and len(self.value) >= 2:
			raise NotImplementedError
		ret = ''.join(str(i) for i in self.value)
		return ret

	def append(self, value):
		self.value.append(value)


class Matrix:

	def __init__(self, value: Union[list, str, int] = None):

		if value is None:
			value = [['A', 'B', 'C', 'D', None],
			         ['E', 'F', 'G', 'H', 'I'],
			         ['J', 'K', 'L', 'M', None]]
		# self.value_raw: List[Union[str, int]] = self._get_raw_from_value(value)
		self.value_raw = value

		self.value_depth = self._get_nesting_depth(value)
		self.matrix: List[Vector] = self._generate_matrix_from_value(value, self.value_depth)
		self.col_count = self._get_col_count(value, self.value_depth)
		# self.row_count = len(value) if value else 1
		self.row_count = self._get_row_count(self.value_raw)

	def _get_raw_from_value(self, value) -> List[Union[str, int]]:
		raise NotImplementedError("_get_raw_from_value")

	@staticmethod
	def _get_row_count(value):
		return len(value) if any(isinstance(i, list) for i in value) else 1

	def _get_col_count(self, value_raw, value_depth):
		# warn("DO ITERATIVE INSTEAD OF RECURSIVE '_get_col_count'")
		col_count = 0
		if value_depth == 0:
			col_count = 1
		elif value_depth == 1:
			col_count = len(value_raw)

		elif value_depth == 2:
			for col in value_raw:
				col_count_temp = self._get_col_count(col, 1)
				col_count = col_count_temp if col_count_temp > col_count else col_count

		return col_count

	# self.matrix: List[self.Row] = []
	# if isinstance(value, list):
	# 	# got a list of something
	# 	if any(isinstance(item, self.Row) for item in value):
	# 		# list of Rows
	# 		if any(not isinstance(item, self.Row) for item in value):
	# 			# shouldn't happen
	# 			raise TypeError('got MIXED ROW AND STR WAT')
	# 		for item in value:
	# 			# append the Row items, no need to box them
	# 			self.matrix.append(item)
	# 	else:
	# 		# list of non-Rows
	# 		for item in value:
	# 			# box the items in Rows and append results
	# 			self.matrix.append(self.Row(item))
	# else:
	# 	if isinstance(value, self.Row):
	# 		raise TypeError('GOT A SINGLE Row handle me')
	# 	else:
	# 		self.matrix.append(self.Row(value))

	# test 5
	def _generate_matrix_from_value(self, value, value_depth) -> List[Vector]:
		matrix: List[Vector] = [[]]
		if value_depth == 0:
			matrix[0].append(Vector(value))
		elif value_depth == 1:
			matrix[0] = Vector(value)
		elif value_depth == 2:
			matrix = [Vector(i) for i in value]
		else:
			value_2d = self._to_2d(value, value_depth)
			matrix = value_2d
			raise NotImplementedError("3d+ to 2d conversion not implemented yet.")

		return matrix

	def _to_2d(self, value, value_depth=None) -> List[Vector]:
		if value_depth is not None:
			for d1 in value:
				for d2 in value:
					print('not implemented yet')

		else:
			value_depth = self._get_nesting_depth(value)
			return self._to_2d(value, value_depth)

	def _get_nesting_depth(self, value):
		# TODO: unequal depths, i.e. [1,[a,b,c]]
		# warn("DO ITERATIVE INSTEAD OF RECURSIVE '_get_nesting_depth'")
		depth_count = 0
		if isinstance(value, list):
			depth_count += 1
			if value:
				depth_count += self._get_nesting_depth(value[0])

		return depth_count

	def extend(self, src, other):
		other_depth = self._get_nesting_depth(other)
		if other_depth < 2:
			raise TypeError("must get 2d+ matrix")
		elif other_depth == 2:
			[src.append(row) for row in other]
		else:
			print("got 3d+ matrix, not implemented")
		return src

	@staticmethod
	def remove_redundant_nesting(value):
		"""
		Return [...] if value is [[...]] (single list in a list)
		"""
		if isinstance(value, list) and len(value) == 1:
			print("Removed redundant nesting")
			ret = value[0]
		else:
			ret = value

		return ret

	# test 5
	# def _get_raw_value(self, value):
	# 	"""
	# 	Extract a list of builtins from a list of Rows (if needed)
	# 	"""
	# 	if isinstance(value, list):
	# 		value_raw = []
	# 		for item in value:
	# 			if isinstance(item, list):
	# 				value_raw.append(item)
	# 			else:
	# 				value_raw.append(item)
	# 	elif isinstance(value, list):
	# 		value_raw = value
	# 	else:
	# 		value_raw = value
	#
	# 	return value_raw

	def __getitem__(self, item):

		# [?,?]
		if isinstance(item, tuple):
			(i, j) = item

			# [?:?:? , ?]
			if isinstance(i, slice):
				temp = self[i]

				# [: , :-1:2]
				# #[['A', 'E', 'J'],
				#  ['C', 'G', 'L']]
				if all(_ is None for _ in (i.start, i.stop, i.step)):
					transposed = self.transpose(temp)
					ret = transposed[j]

				# [1:, :]
				# [['E', 'F', 'G', 'H', 'I'],
				# ['J', 'K', 'L', 'M', None]],
				elif all(_ is None for _ in (j.start, j.stop, j.step)):
					ret = temp

				# [0:2, 0:3]
				# [['A', 'B', 'C'],
				# ['E', 'F', 'G']]
				else:
					for vec_idx, vec in enumerate(temp):
						# TODO: NOT HACKY KAKY!!!
						sliced = vec[j]
						if isinstance(sliced, list):
							temp[vec_idx].value = sliced
						else:
							temp[vec_idx] = sliced
					# temp[vec_idx] = temp[vec_idx][j]
					# [v.value.remove(i) for i in v[j]]
					ret = temp

			# [1 , ?:?:?]
			elif isinstance(j, slice):

				# [1,:] ['E', 'F', 'G', 'H', 'I']
				if all(_ is None for _ in (j.start, j.stop, j.step)):
					ret = self.matrix[i]
				else:
					raise NotImplementedError

			else:
				ret = self.matrix[i][j]

		# [?:?:?]
		elif isinstance(item, slice):

			# [:]    SPECIAL CASE: shallow copy
			if all(_ is None for _ in (item.start, item.stop, item.step)):
				from copy import copy
				ret = copy(self)

			# [-1:3:1] ['J', 'K', 'L', 'M', None]
			else:
				ret = self.matrix[item]
				ret = self.remove_redundant_nesting(ret)


		# [1] ['E', 'F', 'G', 'H', 'I']
		else:
			ret = self.matrix[item]

		return ret

	# if j in self.columns:
	# 	# 'j0'
	# 	if i in self.index:
	# 		# 'i0','j0'
	# 		return self.at[i, j]
	# 	elif isinstance(i, int):
	# 		# 0,'j0'
	# 		return self[j][i]
	# elif isinstance(j, int):

	# 	# j=0
	# 	if isinstance(i, int):
	# 		# 0,0
	# 		return self.iat[i, j]
	# 	elif i in self.index:
	# 		# 'i0',0
	# 		return self[j][i]

	def __str__(self):
		max_len = self._get_max_item_len(self.value_raw)

		def add_h_line(s):
			return strhelp.concat(s, "\n", "  \t",
			                      "-" * (self.col_count * (max_len + 2) + max_len))

		ret = "  \t "

		# column titles
		for i in range(self.col_count):
			ret = strhelp.concat(ret, i, (max_len + 2) * " ")

		ret = add_h_line(ret)

		for i, row in enumerate(self.matrix):
			row_str = f"{i}\t"
			for item in row:
				cell_width = max_len - len(str(item)) + 2
				extra_spaces = cell_width * " "
				row_str = strhelp.concat(row_str, "|", item, extra_spaces)
			ret = strhelp.concat_line(ret, row_str)
			ret = add_h_line(ret)
		return ret

	def __eq__(self, other):
		if isinstance(other, Matrix):
			return ((self.value_raw == other.value_raw) and (
					self.value_depth == other.value_depth) and (
					        self.matrix == other.matrix) and (
					        self.col_count == other.col_count) and (
					        self.row_count == other.row_count))
		else:
			other_depth = self._get_nesting_depth(other)
			return ((self.value_raw == other) and (
					self.value_depth == other_depth) and (
					        self.col_count == self._get_col_count(other, other_depth)) and (
					        self.row_count == self._get_row_count(other)))

	def _get_col_raw(self, col_idx):
		col_ret = []
		for row in self.value_raw:
			col_ret.append(row[col_idx])
		return col_ret

	# no usage
	def _get_transform_raw(self):
		# TODO: try to prevent un/boxing, manipulate without extracting to raw etc
		trans_values = []
		for i in range(self.col_count):
			trans_row = []
			for j in range(self.row_count):
				trans_row.append(self.value_raw[j][i])
			trans_values.append(trans_row)

		# trans_matrix = Matrix(trans_values)

		return trans_values

	@staticmethod
	def transpose(collection):
		if isinstance(collection, Matrix):
			ret = list(map(list, zip(*collection.value_raw)))
		else:
			ret = list(map(list, zip(*collection)))
		return Matrix(ret)

	# def _get_transpose(self):
	#
	# 	trans_values = []
	# 	for i in range(self.col_count):
	# 		trans_row = []
	# 		for j in range(self.row_count):
	# 			trans_row.append(self.value_raw[j][i])
	# 		trans_values.append(trans_row)
	#
	# 	trans_matrix = Matrix(trans_values)
	#
	# 	return trans_matrix

	def _get_max_item_len(self, value):
		"""Get the length of the longest item.
		 Agnostic to number of dimensions"""
		# TODO: Do iterative instead of recursive
		# warn("CHANGE '_get_max_item_len' to ITERATIVE")
		max_len = 0
		if isinstance(value, list):
			if value:
				for item in value:
					res = self._get_max_item_len(item)
					if res > max_len:
						max_len = res

		else:
			return len(str(value))

		return max_len


# if __name__ == '__main__.matrix':
# 	Matrix()
# m4 = Matrix(["A", "B"])
# print(m4.row_count)
m = Matrix()
print(m)
# print(m4.transform())
# print(m4[0, 0])
# print(m4[:-2])
# print(m4[1, -1])
# print(m4[1])
# print(m4[:2])
# print(m4[0][2:])
# print(m4[:][1])
# print(m4[2][::2])
# print(m4[:])
# todo: There are two types of advanced indexing: integer and Boolean
# todo: [-3:3:2]
# todo: insert single value to constructor
# todo: 3d+ container
# todo: m4.matrix is a list of Row
# todo: m_test.matrix is a list of lists of Row
# todo: add tests to send single Row types
# todo: add tests for get empty lists
# m_test = m4[:2]
# print(f"pre:\n{m_test}")
# m_test = m_test.transform()
# print(f"\npost:\n{m_test}")
# m2_test = m_test[1:3]
# print(m2_test)
# print(m4[:2][1:3])
