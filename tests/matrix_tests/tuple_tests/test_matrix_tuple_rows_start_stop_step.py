from ...boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_1_colon_3_colon_1():
	bp.basic_test(res=bp.m[1:3:1, :],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list)


def test_rev1_colon_3_colon_1():
	bp.basic_test(res=bp.m[-1:3:1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_1_colon_rev1_colon_1():
	bp.basic_test(res=bp.m[1:-1:1, :],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=Vector)


def test_rev3_colon_rev1_colon_1():
	bp.basic_test(res=bp.m[-3:-1:1, :],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)


def test_1_colon_1_colon_rev1():
	bp.basic_test(res=bp.m[2:1:-1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_rev1_colon_1_colon_rev1():
	bp.basic_test(res=bp.m[-1:1:-1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)


def test_1_colon_rev4_colon_rev1():
	bp.basic_test(res=bp.m[1:-4:-1, :],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)


def test_rev1_colon_rev4_colon_rev2():
	bp.basic_test(res=bp.m[-1:-4:-2, :],
	                 expected=[['J', 'K', 'L', 'M', None],
	                           ['A', 'B', 'C', 'D', None]],
	                 res_type=list)
