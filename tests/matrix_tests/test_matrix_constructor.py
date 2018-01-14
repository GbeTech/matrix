from src.matrix import Matrix, Vector
from ..setup import Setup

setup = Setup()


# INIT TESTS
def test_init_0D():
	setup.basic_test(res=Matrix("A"),
	                 expected="A",
	                 res_type=str)


def test_init_1D():
	setup.basic_test(res=Matrix(["A", "B"]),
	                 expected=[["A", "B"]],
	                 res_type=Vector)


def test_init_2D():
	setup.basic_test(res=Matrix([["A", "B"],
	                             ["C", "D"]]),
	                 expected=[["A", "B"],
	                           ["C", "D"]],
	                 res_type=list)
