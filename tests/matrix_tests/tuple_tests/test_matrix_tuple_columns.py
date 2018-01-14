from ...boilerplate import Boilerplate
from src.matrix import Vector

bp = Boilerplate()


def test_tuple_column_1():
	bp.basic_test(res=bp.m[:, 1],
	              expected=['B', 'F', 'K'],
	              res_type=Vector)


def test_tuple_column_rev1():
	bp.basic_test(res=bp.m[:, -1],
	              expected=[None, 'I', None],
	              res_type=Vector)
