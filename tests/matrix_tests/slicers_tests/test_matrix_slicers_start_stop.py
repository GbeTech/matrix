from ...boilerplate import Boilerplate


bp = Boilerplate()


def test_1_colon_2():
	bp.basic_test(res=bp.m[1:2],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=list)


def test_0_colon_rev2():
	bp.basic_test(res=bp.m[0:-1],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)


def test_rev1_colon_3():
	bp.basic_test(res=bp.m[-1:3],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=list)


def test_rev3_colon_rev1():
	bp.basic_test(res=bp.m[-3:-1],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)
