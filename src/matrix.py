from typing import List, Union
from helpers import strhelp


class Matrix:

	def __init__(self, value: Union[list, str, int] = None):

		if value is None:
			value = [['A', 'B', 'C', 'D', None],
			         ['E', 'F', 'G', 'H', 'I'],
			         ['J', 'K', 'L', 'M', None]]
		self.value_raw = value

		self.value_depth = self._get_list_depth(value)
		self.matrix: List[list] = self._generate_matrix_from_value(value, self.value_depth)
		self.col_count = self._get_col_count(value, self.value_depth)
		self.row_count = self._get_row_count(self.value_raw)

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

	def _generate_matrix_from_value(self, value, value_depth) -> List[list]:
		matrix = [[]]
		if value_depth == 0:
			matrix[0].append(value)
		elif value_depth == 1:
			matrix[0] = value
		elif value_depth == 2:
			matrix = value
		else:
			raise NotImplementedError("3d+ to 2d conversion not implemented yet.")

		return matrix

	def _get_list_depth(self, value):
		depth_count = 0
		if isinstance(value, list):
			depth_count += 1
			depth_count += self._get_list_depth(value[0])

		return depth_count

	@staticmethod
	def remove_redundant_nesting(value):
		"""
		Return [...] if value is [[...]] (single list in a list)
		"""
		if isinstance(value, list) and len(value) == 1:
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
					# [?,?,...]
					if isinstance(temp, list):
						# [[?],[?]] -> 2D
						if any(isinstance(vec, list) for vec in temp):
							for vec_idx, vec in enumerate(temp):
								temp[vec_idx] = vec[j]
						# [?,?] -> 1D
						else:
							temp = temp[j]
					else:
						raise NotImplementedError('shouldnt happen')
					ret = temp


			# [0,???]
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
			return self.value_raw == other.value_raw
		else:
			return self.value_raw == other

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

	# USAGE ONLY IN STR
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
