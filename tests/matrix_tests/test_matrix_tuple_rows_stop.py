from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_colon_2():
	setup.basic_test(res=setup.m[:2, :],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)


def test_colon_rev2():
	setup.basic_test(res=setup.m[:-2, :],
	                 expected=['A', 'B', 'C', 'D', None],
	                 res_type=Vector)
