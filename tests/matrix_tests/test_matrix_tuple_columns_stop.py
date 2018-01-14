from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_tuple_colon_1():
	setup.basic_test(res=setup.m[:, :2],
	                 expected=[['A', 'E', 'J'],
	                           ['B', 'F', 'K']],
	                 res_type=list)


def test_tuple_colon_rev1():
	setup.basic_test(res=setup.m[:, :-2],
	                 expected=[['A', 'E', 'J'],
	                           ['B', 'F', 'K'],
	                           ['C', 'G', 'L']],
	                 res_type=list)
