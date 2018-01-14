from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_0_colon_rev2():
	setup.basic_test(res=setup.m[:, 0:-3],
	                 expected=[['A', 'E', 'J'],
	                           ['B', 'F', 'K']],
	                 res_type=list)


def test_rev1_colon_3():
	setup.basic_test(res=setup.m[:, -1:5],
	                 expected=[None, 'I', None],
	                 res_type=Vector)


def test_rev3_colon_rev1():
	setup.basic_test(res=setup.m[:, -3:-1],
	                 expected=[['C', 'G', 'L'],
	                           ['D', 'H', 'M']],
	                 res_type=list)
