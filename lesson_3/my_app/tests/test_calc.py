import pytest
from src.calc import Calc


class TestCalc():
    
    def test_sum_simple(self):
        calc = Calc()

        assert calc.sum(5, 5) == 10

    def test_sum_another_sum(self):
        calc = Calc()

        assert calc.sum(3, 2) == 5

    def test_sub_simple(self):
        calc = Calc()

        assert calc.sub(1, 2) == -1

    def test_sub_another(self):
        calc = Calc()

        assert calc.sub(50, 50) == 0

    def test_div_simple(self):
        calc = Calc()

        assert calc.divisoin(10, 5) == 2

    def test_div_by_zero(self):
        calc = Calc()
        with pytest.raises(ZeroDivisionError):
            assert calc.divisoin(10 / 0)
