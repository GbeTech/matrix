from ...boilerplate import Boilerplate


bp = Boilerplate()


def test_colon_1_colon_1():
	bp.basic_test(res=bp.m[:, :1:1],
	              expected=['A', 'E', 'J'],
	              res_type=list)


def test_colon_1_colon_rev1():
	bp.basic_test(res=bp.m[:, :1:-2],
	              expected=[[None, 'I', None],
	                        ['C', 'G', 'L']],
	              res_type=list)


def test_colon_rev1_colon_2():
	bp.basic_test(res=bp.m[:, :-1:2],
	              expected=[['A', 'E', 'J'],
	                        ['C', 'G', 'L']],
	              res_type=list)


def test_colon_rev4_colon_rev1():
	bp.basic_test(res=bp.m[:, :-3:-1],
	              expected=[[None, 'I', None],
	                        ['D', 'H', 'M']],
	              res_type=list)
