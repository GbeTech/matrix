from ...boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_1_dcolon_2():
	bp.basic_test(res=bp.m[1::2],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=Vector)


def test_1_dcolon_rev1():
	bp.basic_test(res=bp.m[1::-1],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)


def test_rev3_dcolon_rev2():
	bp.basic_test(res=bp.m[-3::2],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list)


def test_rev2_dcolon_rev1():
	bp.basic_test(res=bp.m[-2::-1],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)
