from ...boilerplate import Boilerplate
from src.matrix import Matrix

bp = Boilerplate()


def test_dcolon_1():
	bp.basic_test(res=bp.m[:, ::1],
	              expected=[['A', 'E', 'J'],
	                        ['B', 'F', 'K'],
	                        ['C', 'G', 'L'],
	                        ['D', 'H', 'M'],
	                        [None, 'I', None]],
	              res_type=list)


def test_dcolon_2():
	bp.basic_test(res=bp.m[:, ::2],
	              expected=[['A', 'E', 'J'],
	                        ['C', 'G', 'L'],
	                        [None, 'I', None]],
	              res_type=list)


def test_dcolon_rev1():
	bp.basic_test(res=bp.m[:, ::-3],
	              expected=[[None, 'I', None],
	                        ['B', 'F', 'K']],
	              res_type=list)


def test_get_shallow_copy():
	bp.basic_test(res=bp.m[:, :],
	              expected=[['A', 'E', 'J'],
	                        ['B', 'F', 'K'],
	                        ['C', 'G', 'L'],
	                        ['D', 'H', 'M'],
	                        [None, 'I', None]],
	              res_type=Matrix)
