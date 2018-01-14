from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_1_colon_2():
	setup.basic_test(res=setup.m[1:2, :],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=Vector)


def test_0_colon_rev2():
	setup.basic_test(res=setup.m[0:-1, :],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)


def test_rev1_colon_3():
	setup.basic_test(res=setup.m[-1:3, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_rev3_colon_rev1():
	setup.basic_test(res=setup.m[-3:-1, :],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)
