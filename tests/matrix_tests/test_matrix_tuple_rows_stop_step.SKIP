from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_colon_1_colon_1():
	setup.basic_test(res=setup.m[:1:1, :],
	                 expected=['A', 'B', 'C', 'D', None],
	                 res_type=Vector)


def test_colon_1_colon_rev1():
	setup.basic_test(res=setup.m[:1:-1],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_colon_rev1_colon_2():
	setup.basic_test(res=setup.m[:-1:2],
	                 expected=['A', 'B', 'C', 'D', None],
	                 res_type=Vector)


def test_colon_rev4_colon_rev1():
	setup.basic_test(res=setup.m[:-4:-1],
	                 expected=[['J', 'K', 'L', 'M', None],
	                           ['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list,
	                 index_type_pairs={0: Vector, 1: Vector, 2: Vector})
