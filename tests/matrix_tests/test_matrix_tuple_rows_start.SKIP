from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_tuple_1_colon():
	setup.basic_test(res=setup.m[1:, :],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list)


def test_tuple_rev1_colon():
	setup.basic_test(res=setup.m[-3:, :],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list)

	setup.not_is_equal(setup.m[-3:, :], setup.m)
