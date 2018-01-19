from ...boilerplate import Boilerplate

bp = Boilerplate()


def test_tuple_1_colon():
	bp.basic_test(res=bp.m[1:, :],
	              expected=[['E', 'F', 'G', 'H', 'I'],
	                        ['J', 'K', 'L', 'M', None]],
	              res_type=list)


def test_tuple_rev1_colon():
	bp.basic_test(res=bp.m[-3:, :],
	              expected=[['A', 'B', 'C', 'D', None],
	                        ['E', 'F', 'G', 'H', 'I'],
	                        ['J', 'K', 'L', 'M', None]],
	              res_type=list)

	bp.not_is_a(bp.m[-3:, :], bp.m)
