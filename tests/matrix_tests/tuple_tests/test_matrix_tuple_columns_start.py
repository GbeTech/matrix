from ...boilerplate import Boilerplate

bp = Boilerplate()


def test_tuple_colon_1():
	bp.basic_test(res=bp.m[:, 1:],
	              expected=[['B', 'F', 'K'],
	                        ['C', 'G', 'L'],
	                        ['D', 'H', 'M'],
	                        [None, 'I', None]],
	              res_type=list)


def test_tuple_colon_rev1():
	bp.basic_test(res=bp.m[:, -2:],
	              expected=[['D', 'H', 'M'],
	                        [None, 'I', None]],
	              res_type=list)
