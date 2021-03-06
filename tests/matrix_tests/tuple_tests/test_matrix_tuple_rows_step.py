from ...boilerplate import Boilerplate
from src.matrix import Matrix, Vector

bp = Boilerplate()


def test_dcolon_1():
	bp.basic_test(res=bp.m[::1, :],
	              expected=[['A', 'B', 'C', 'D', None],
	                        ['E', 'F', 'G', 'H', 'I'],
	                        ['J', 'K', 'L', 'M', None]],
	              res_type=list)


def test_dcolon_2():
	bp.basic_test(res=bp.m[::2],
	              expected=[['A', 'B', 'C', 'D', None],
	                        ['J', 'K', 'L', 'M', None]],
	              res_type=list)


# NOT transformation
def test_dcolon_rev1():
	bp.basic_test(res=bp.m[::-1],
	              expected=[['J', 'K', 'L', 'M', None],
	                        ['E', 'F', 'G', 'H', 'I'],
	                        ['A', 'B', 'C', 'D', None]],
	              res_type=list)


def test_dcolon_rev2():
	bp.basic_test(res=bp.m[::-2],
	              expected=[['J', 'K', 'L', 'M', None],
	                        ['A', 'B', 'C', 'D', None]],
	              res_type=list)


def test_get_shallow_copy():
	bp.basic_test(res=bp.m[:],
	              expected=[['A', 'B', 'C', 'D', None],
	                        ['E', 'F', 'G', 'H', 'I'],
	                        ['J', 'K', 'L', 'M', None]],
	              res_type=Matrix,
	              index_type_pairs={0: Vector, 1: Vector, 2: Vector})

	bp.not_is_a(bp.m[:], bp.m)
