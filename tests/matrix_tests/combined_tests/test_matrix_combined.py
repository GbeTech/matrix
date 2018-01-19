from ...boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_01():
	bp.basic_test(res=bp.m[0:2, 0:3],
	              expected=[['A', 'B', 'C'],
	                        ['E', 'F', 'G']],
	              res_type=list)


def test_02():
	bp.basic_test(res=bp.m[1::2, 0:3],
	              expected=['E', 'F', 'G'],
	              res_type=Vector)


def test_03():
	bp.basic_test(res=bp.m[2::, 1::],
	              expected=['K', 'L', 'M', None],
	              res_type=Vector)

# def test_rev1_colon_rev4_colon_rev2():
# 	bp.basic_test(res=bp.m[-1::-2, -2::-2],
# 	              expected=[['M', 'K'],
# 	                        ['D', 'B']],
# 	              res_type=list)
