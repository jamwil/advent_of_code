"""Unit tests for Advent of Code 2022 Day 3."""
from main import sum_item_priority, _create_item_priority_map


CONTENTS = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


def test_create_item_priority_map():
    """Test that the create_item_priority_map function returns the correct value."""
    mapping = _create_item_priority_map()
    assert mapping["p"] == 16
    assert mapping["L"] == 38


def test_main():
    """Test that the main function returns the correct value."""
    assert sum_item_priority(CONTENTS) == 157
