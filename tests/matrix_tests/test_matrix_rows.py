from ..boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_1():
	bp.basic_test(res=bp.m[1],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=Vector)


def test_rev1():
	bp.basic_test(res=bp.m[-1],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=Vector)
