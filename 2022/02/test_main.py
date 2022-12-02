"""Test Day 2 of Advent of Code."""
from main import calculate_score_1, calculate_score_2

STRATEGY_GUIDE = """
A Y
B X
C Z
""".strip()


def test_calculate_score_1():
    """Test the scoring algorithm per a given strategy guide."""
    assert calculate_score_1(STRATEGY_GUIDE) == 15


def test_calculate_score_2():
    """Test the scoring algorithm with a different column B meaning."""
    assert calculate_score_2(STRATEGY_GUIDE) == 12
