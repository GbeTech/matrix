from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_tuple_colon_1():
	setup.basic_test(res=setup.m[:, 1],
	                 expected=['B', 'F', 'K'],
	                 res_type=Vector)


def test_tuple_colon_rev1():
	setup.basic_test(res=setup.m[:, -1],
	                 expected=[None, 'I', None],
	                 res_type=Vector)
