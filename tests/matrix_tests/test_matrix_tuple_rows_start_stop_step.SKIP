from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_1_colon_3_colon_1():
	setup.basic_test(res=setup.m[1:3:1, :],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list)


def test_rev1_colon_3_colon_1():
	setup.basic_test(res=setup.m[-1:3:1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_1_colon_rev1_colon_1():
	setup.basic_test(res=setup.m[1:-1:1, :],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=Vector)


def test_rev3_colon_rev1_colon_1():
	setup.basic_test(res=setup.m[-3:-1:1, :],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)


def test_1_colon_1_colon_rev1():
	setup.basic_test(res=setup.m[2:1:-1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_rev1_colon_1_colon_rev1():
	setup.basic_test(res=setup.m[-1:1:-1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_1_colon_rev4_colon_rev1():
	setup.basic_test(res=setup.m[1:-4:-1, :],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)


def test_rev1_colon_rev4_colon_rev2():
	setup.basic_test(res=setup.m[-1:-4:-2, :],
	                 expected=[['J', 'K', 'L', 'M', None],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)
