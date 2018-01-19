from ...boilerplate import Boilerplate


bp = Boilerplate()


def test_tuple_1():
	bp.basic_test(res=bp.m[1, :],
	                 expected=['E', 'F', 'G', 'H', 'I'],
	                 res_type=list)


def test_tuple_rev1():
	bp.basic_test(res=bp.m[-1, :],
	                 expected=['J', 'K', 'L', 'M', None],
	                 res_type=list)
