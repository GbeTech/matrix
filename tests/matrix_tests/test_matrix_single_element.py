from ..boilerplate import Boilerplate

bp = Boilerplate()


def test_0_0():
	bp.basic_test(res=bp.m[0, 0],
	              expected='A',
	              res_type=str)


def test_1_rev1():
	bp.basic_test(res=bp.m[1, -1],
	              expected='I',
	              res_type=str)


def test_rev1_1():
	bp.basic_test(res=bp.m[-1, 1],
	              expected='K',
	              res_type=str)


# DIDN'T PASS
def test_rev1_rev1():
	bp.basic_test(res=bp.m[-1, -1],
	              expected=None,
	              res_type=None)
