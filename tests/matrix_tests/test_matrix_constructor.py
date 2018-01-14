from src.matrix import Matrix, Vector
from ..boilerplate import Boilerplate

bp = Boilerplate()


# INIT TESTS
def test_init_0D():
	bp.basic_test(res=Matrix("A"),
	              expected="A",
	              res_type=Matrix)


def test_init_1D():
	bp.basic_test(res=Matrix(["A", "B"]),
	              expected=["A", "B"],
	              res_type=Matrix)


def test_init_2D():
	bp.basic_test(res=Matrix([["A", "B"],
	                          ["C", "D"]]),
	              expected=[["A", "B"],
	                        ["C", "D"]],
	              res_type=Matrix)
