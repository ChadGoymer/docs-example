# \tests\test_calculations.py

import pytest

from calculator.calculations import add


class TestAdd:
    """Testing the add() function"""

    def test_add_integer(self):
        """Test adding two integers"""
        assert add(1, 1) == 2

    def test_add_float(self):
        """Test adding two floats"""
        assert add(1.0, 1.0) == 2.0

    def test_add_invalid_number(self):
        """Test adding an integer and a string produces a TypeError"""
        with pytest.raises(TypeError):
            add(1, "1")  # type: ignore
