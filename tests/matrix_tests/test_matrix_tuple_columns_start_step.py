from tests.setup import Setup
from src.matrix import Vector

setup = Setup()


def test_1_dcolon_2():
	setup.basic_test(res=setup.m[:, 1::2],
	                 expected=[['B', 'F', 'K'],
	                           ['D', 'H', 'M']],
	                 res_type=list)


def test_1_dcolon_rev1():
	setup.basic_test(res=setup.m[:, 1::-1],
	                 expected=[['B', 'F', 'K'],
	                           ['A', 'E', 'J']],
	                 res_type=list)


def test_rev3_dcolon_rev2():
	setup.basic_test(res=setup.m[:, -3::2],
	                 expected=[['C', 'G', 'L'],
	                           [None, 'I', None]],
	                 res_type=list)


def test_rev2_dcolon_rev1():
	setup.basic_test(res=setup.m[:, -2::-1],
	                 expected=[['D', 'H', 'M'],
	                           ['B', 'F', 'K']],
	                 res_type=list)
