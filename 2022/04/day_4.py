"""Day 4 of Advent of Code 2022."""
from pathlib import Path


def count_subsets(assignments):
    """Count the number of assignment pairs that are a subset of one another."""
    subset_count = 0

    assignment_pairs = assignments.splitlines()
    for assignment_pair in assignment_pairs:
        elf_1_range, elf_2_range = assignment_pair.split(",")
        elf_1 = set(
            range(int(elf_1_range.split("-")[0]), int(elf_1_range.split("-")[1]) + 1)
        )
        elf_2 = set(
            range(int(elf_2_range.split("-")[0]), int(elf_2_range.split("-")[1]) + 1)
        )
        intersect = elf_1 & elf_2
        if intersect == elf_1 or intersect == elf_2:
            subset_count += 1

    return subset_count


def count_intersects(assignments):
    """Count the number of overlapping assignment pairs."""
    intersect_count = 0

    assignment_pairs = assignments.splitlines()
    for assignment_pair in assignment_pairs:
        elf_1_range, elf_2_range = assignment_pair.split(",")
        elf_1 = set(
            range(int(elf_1_range.split("-")[0]), int(elf_1_range.split("-")[1]) + 1)
        )
        elf_2 = set(
            range(int(elf_2_range.split("-")[0]), int(elf_2_range.split("-")[1]) + 1)
        )
        intersect = elf_1 & elf_2
        if intersect:
            intersect_count += 1

    return intersect_count


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file, "r", encoding="utf-8") as f:
        input_data = f.read()
    print("Part 1:", count_subsets(input_data))
    print("Part 2:", count_intersects(input_data))
