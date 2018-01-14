from ...boilerplate import Boilerplate

bp = Boilerplate()


def test_1_dcolon_2():
	bp.basic_test(res=bp.m[:, 1::2],
	              expected=[['B', 'F', 'K'],
	                        ['D', 'H', 'M']],
	              res_type=list)


def test_1_dcolon_rev1():
	bp.basic_test(res=bp.m[:, 1::-1],
	              expected=[['B', 'F', 'K'],
	                        ['A', 'E', 'J']],
	              res_type=list)


def test_rev3_dcolon_rev2():
	bp.basic_test(res=bp.m[:, -3::2],
	              expected=[['C', 'G', 'L'],
	                        [None, 'I', None]],
	              res_type=list)


def test_rev2_dcolon_rev1():
	bp.basic_test(res=bp.m[:, -2::-1],
	              expected=[['D', 'H', 'M'],
	                        ['C', 'G', 'L'],
	                        ['B', 'F', 'K'],
	                        ['A', 'E', 'J']],
	              res_type=list)


def test_rev2_dcolon_rev2():
	bp.basic_test(res=bp.m[:, -2::-2],
	              expected=[['D', 'H', 'M'],
	                        ['B', 'F', 'K']],
	              res_type=list)
