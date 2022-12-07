"""Unit tests for Day 6."""
from day_6 import subroutine

BUFFER = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_subroutine():
    """Test part 1."""
    assert subroutine(BUFFER, 4) == 7
    assert subroutine(BUFFER, 14) == 19
