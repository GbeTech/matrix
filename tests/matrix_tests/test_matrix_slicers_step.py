from ..setup import Setup
from src.matrix import Matrix, Vector

setup = Setup()


def test_dcolon_1():
	setup.basic_test(res=setup.m[::1],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list,
	                 index_type_pairs={0: Vector, 1: Vector, 2: Vector})


def test_dcolon_2():
	setup.basic_test(res=setup.m[::2],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list,
	                 index_type_pairs={0: Vector, 1: Vector})


# NOT transformation
def test_dcolon_rev1():
	setup.basic_test(res=setup.m[::-1],
	                 expected=[['J', 'K', 'L', 'M', None],
	                           ['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list,
	                 index_type_pairs={0: Vector, 1: Vector, 2: Vector})


def test_dcolon_rev2():
	setup.basic_test(res=setup.m[::-2],
	                 expected=[['J', 'K', 'L', 'M', None],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list,
	                 index_type_pairs={0: Vector, 1: Vector})


def test_get_shallow_copy():
	setup.basic_test(res=setup.m[:],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=Matrix,
	                 index_type_pairs={0: Vector, 1: Vector, 2: Vector})

	setup.not_is_equal(setup.m[:], setup.m)
