from ..boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_colon_2():
	bp.basic_test(res=bp.m[:2],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list,
	                 index_type_pairs={0: Vector, 1: Vector})


def test_colon_rev2():
	bp.basic_test(res=bp.m[:-2],
	                 expected=['A', 'B', 'C', 'D', None],
	                 res_type=Vector)
