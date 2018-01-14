from ..boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_1_colon():
	bp.basic_test(res=bp.m[1:],
	                 expected=[['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list)


def test_rev1_colon():
	bp.basic_test(res=bp.m[-3:],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I'],
	                           ['J', 'K', 'L', 'M', None]],
	                 res_type=list,
	                 index_type_pairs={0: Vector, 1: Vector, 2: Vector})

	# shallow copy
	bp.not_is_equal(bp.m[-3:], bp.m)
