import pytest

from ..calc_shapes import CalcShapes


@pytest.fixture()
def shapes() -> CalcShapes:
    return CalcShapes()
