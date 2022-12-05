"""Unit tests for Advent of Code Day 4."""
from day_4 import count_subsets, count_intersects

ASSIGNMENTS = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


def test_count_subsets():
    """Test that overlapping assignment pairs are found."""
    assert count_subsets(ASSIGNMENTS) == 2


def test_count_intersects():
    """Test that overlapping assignment pairs are found."""
    assert count_intersects(ASSIGNMENTS) == 4
