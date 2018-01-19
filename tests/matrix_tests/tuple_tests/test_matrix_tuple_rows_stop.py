from ...boilerplate import Boilerplate


bp = Boilerplate()


def test_colon_2():
	bp.basic_test(res=bp.m[:2, :],
	                 expected=[['A', 'B', 'C', 'D', None],
	                           ['E', 'F', 'G', 'H', 'I']],
	                 res_type=list)


def test_colon_rev2():
	bp.basic_test(res=bp.m[:-2, :],
	                 expected=['A', 'B', 'C', 'D', None],
	                 res_type=list)
