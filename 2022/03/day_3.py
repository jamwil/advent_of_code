"""Advent of Code 2022 Day 3."""
from pathlib import Path


def _create_item_priority_map() -> dict[str, int]:
    """Create a map of item to priority."""
    mapping = {}
    for priority, char in enumerate(range(ord("a"), ord("z") + 1), start=1):
        mapping[chr(char)] = priority
    for priority, char in enumerate(range(ord("A"), ord("Z") + 1), start=27):
        mapping[chr(char)] = priority
    return mapping


def sum_item_priority(rucksacks: str) -> int:
    """Return the sum of the item priority."""
    common_items = []
    for rucksack in rucksacks.splitlines():
        divider = len(rucksack) // 2
        compartment_1, compartment_2 = set(rucksack[:divider]), set(rucksack[divider:])
        shared_items_in_rucksack = compartment_1 & compartment_2
        if len(shared_items_in_rucksack) != 1:
            raise ValueError("Invalid rucksack")
        common_items.append(shared_items_in_rucksack.pop())
    priority_map = _create_item_priority_map()
    return sum(priority_map[item] for item in common_items)


def sum_item_group_priority(rucksacks: str) -> int:
    """Return the sum of the group item priority."""
    groups = []
    inner = []
    for i, rucksack in enumerate(rucksacks.splitlines(), start=1):
        inner.append(rucksack)
        if i % 3 == 0:
            groups.append(inner)
            inner = []
    common_items = []
    for group in groups:
        shared_items_in_group = set(group[0]) & set(group[1]) & set(group[2])
        if len(shared_items_in_group) != 1:
            raise ValueError("Invalid group")
        common_items.append(shared_items_in_group.pop())
    priority_map = _create_item_priority_map()
    return sum(priority_map[item] for item in common_items)


if __name__ == "__main__":
    input_data = Path(__file__).parent.resolve() / "input.txt"
    with open(input_data, "r", encoding="utf-8") as f:
        contents = f.read()
    print("Part 1:", sum_item_priority(contents))
    print("Part 2:", sum_item_group_priority(contents))
