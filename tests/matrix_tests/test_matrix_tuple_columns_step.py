from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_dcolon_1():
	setup.basic_test(res=setup.m[:, ::1],
	                 expected=[['A', 'E', 'J'],
	                           ['B', 'F', 'K'],
	                           ['C', 'G', 'L'],
	                           ['D', 'H', 'M'],
	                           [None, 'I', None]],
	                 res_type=list)


def test_dcolon_2():
	setup.basic_test(res=setup.m[:, ::2],
	                 expected=[['A', 'E', 'J'],
	                           ['C', 'G', 'L'],
	                           [None, 'I', None]],
	                 res_type=list)


def test_dcolon_rev1():
	setup.basic_test(res=setup.m[::-3],
	                 expected=[[None, 'I', None],
	                           ['B', 'F', 'K']],
	                 res_type=list)


def test_get_shallow_copy():
	setup.basic_test(res=setup.m[:, :],
	                 expected=[['A', 'E', 'J'],
	                           ['B', 'F', 'K'],
	                           ['C', 'G', 'L'],
	                           ['D', 'H', 'M'],
	                           [None, 'I', None]],
	                 res_type=Matrix,
	                 index_type_pairs={0: Vector, 1: Vector, 2: Vector, 3: Vector, 4: Vector})
