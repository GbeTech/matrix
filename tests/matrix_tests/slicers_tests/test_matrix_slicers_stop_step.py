from ...boilerplate import Boilerplate

bp = Boilerplate()


def test_colon_1_colon_1():
	bp.basic_test(res=bp.m[:1:1],
	              expected=['A', 'B', 'C', 'D', None],
	              res_type=list)


def test_colon_1_colon_rev1():
	bp.basic_test(res=bp.m[:1:-1],
	              expected=['J', 'K', 'L', 'M', None],
	              res_type=list)


def test_colon_rev1_colon_2():
	bp.basic_test(res=bp.m[:-1:2],
	              expected=['A', 'B', 'C', 'D', None],
	              res_type=list)


def test_colon_rev4_colon_rev1():
	bp.basic_test(res=bp.m[:-4:-1],
	              expected=[['J', 'K', 'L', 'M', None],
	                        ['E', 'F', 'G', 'H', 'I'],
	                        ['A', 'B', 'C', 'D', None]],
	              res_type=list)
