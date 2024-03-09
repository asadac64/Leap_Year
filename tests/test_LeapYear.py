"""Test cases for Leap Year."""

# Standard libraryy

# 3rd Party library
import pytest

# Project library
from leap_year.leapyear import print_learyear

@pytest.mark.parametrize(
    "year,expected",
    [
        (2024,"Leap Year"),
        (2020,"Leap Year"),
        (2016,"Leap Year"),
        (2023,"Not Leap Year"),
    ]
)
def test_leap_year(year,expected):
    # Arrange
    # Act
    result = print_learyear(year)
    # Assert
    assert result == expected