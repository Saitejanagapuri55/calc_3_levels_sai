import pytest
from calculator import Calculator
from calculation import Calculation
from calculations import Calculations

@pytest.fixture
def setup_calculations():
    Calculations.history.clear()

def test_add(setup_calculations):
    assert Calculator.add(1, 2) == 3

def test_subtract(setup_calculations):
    assert Calculator.subtract(5, 2) == 3

def test_multiply(setup_calculations):
    assert Calculator.multiply(3, 2) == 6

def test_divide(setup_calculations):
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero(setup_calculations):
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)

def test_calculation_history(setup_calculations):
    calc1 = Calculation(1, 2, 'add')
    Calculations.add_calculation(calc1)
    assert Calculations.get_last_calculation() == calc1
