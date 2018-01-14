from ..setup import Setup

setup = Setup()


def test_0_0():
	setup.basic_test(res=setup.m[0, 0],
	                 expected='A',
	                 res_type=str)


def test_1_rev1():
	setup.basic_test(res=setup.m[1, -1],
	                 expected='I',
	                 res_type=str)


def test_rev1_1():
	setup.basic_test(res=setup.m[-1, 1],
	                 expected='K',
	                 res_type=str)


# DIDN'T PASS
def test_rev1_rev1():
	setup.basic_test(res=setup.m[-1, -1],
	                 expected='M',
	                 res_type=str)
