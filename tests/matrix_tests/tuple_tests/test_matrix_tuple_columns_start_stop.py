from ...boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_0_colon_rev2():
	bp.basic_test(res=bp.m[:, 0:-3],
	              expected=[['A', 'E', 'J'],
	                        ['B', 'F', 'K']],
	              res_type=list)


def test_rev1_colon_3():
	bp.basic_test(res=bp.m[:, -1:5],
	              expected=[None, 'I', None],
	              res_type=Vector)


def test_rev3_colon_rev1():
	bp.basic_test(res=bp.m[:, -3:-1],
	              expected=[['C', 'G', 'L'],
	                        ['D', 'H', 'M']],
	              res_type=list)
