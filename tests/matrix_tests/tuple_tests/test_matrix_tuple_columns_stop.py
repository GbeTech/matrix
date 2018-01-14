from ...boilerplate import Boilerplate

bp = Boilerplate()


def test_tuple_colon_1():
	bp.basic_test(res=bp.m[:, :2],
	              expected=[['A', 'E', 'J'],
	                        ['B', 'F', 'K']],
	              res_type=list)


def test_tuple_colon_rev1():
	bp.basic_test(res=bp.m[:, :-2],
	              expected=[['A', 'E', 'J'],
	                        ['B', 'F', 'K'],
	                        ['C', 'G', 'L']],
	              res_type=list)
