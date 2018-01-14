from ..setup import Setup
from src.matrix import Vector

setup = Setup()


def test_1_dcolon_2():
	setup.basic_test(res=setup.m[1::2],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=Vector)


def test_1_dcolon_rev1():
	setup.basic_test(res=setup.m[1::-1],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)


def test_rev3_dcolon_rev2():
	setup.basic_test(res=setup.m[-3::2],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list)


def test_rev2_dcolon_rev1():
	setup.basic_test(res=setup.m[-2::-1],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)
