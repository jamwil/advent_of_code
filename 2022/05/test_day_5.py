"""Unit tests for Advent of Code 2022, day 5."""
from day_5 import get_stack_tops


INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_cratemover9000():
    """Test get_stack_tops."""
    assert get_stack_tops(INPUT, "cratemover9000") == "CMZ"


def test_cratemover9001():
    """Test get_stack_tops."""
    assert get_stack_tops(INPUT, "cratemover9001") == "MCD"
