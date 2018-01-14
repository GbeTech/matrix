from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_tuple_1():
	setup.basic_test(res=setup.m[1, :],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=Vector)


def test_tuple_rev1():
	setup.basic_test(res=setup.m[-1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)
