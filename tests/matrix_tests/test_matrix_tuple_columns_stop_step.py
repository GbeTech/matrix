from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_colon_1_colon_1():
	setup.basic_test(res=setup.m[:, :1:1],
	                 expected=['A', 'E', 'J'],
	                 res_type=Vector)


def test_colon_1_colon_rev1():
	setup.basic_test(res=setup.m[:1:-2],
	                 expected=[[None, 'I', None],
	                           ['C', 'G', 'L']],
	                 res_type=list)


def test_colon_rev1_colon_2():
	setup.basic_test(res=setup.m[:-1:2],
	                 expected=[['A', 'E', 'J'],
	                           ['C', 'G', 'L']],
	                 res_type=Vector)


def test_colon_rev4_colon_rev1():
	setup.basic_test(res=setup.m[:-3:-1],
	                 expected=[[None, 'I', None],
	                           ['D', 'H', 'M']],
	                 res_type=list)
