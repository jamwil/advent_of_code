"""Day 5 of Advent of Code 2022."""
from pathlib import Path
import re
from collections import deque


class Shipyard:
    def __init__(self, stacks_input: list):
        self.stacks = self._ingest_stacks(stacks_input)

    @staticmethod
    def _ingest_stacks(stacks_input: str):
        levels = stacks_input.splitlines()
        stack_labels = levels.pop()
        indices = [i for i, c in enumerate(stack_labels) if c != " "]
        stacks = []
        for index in indices:
            stack = deque()
            for level in reversed(levels):
                if level[index] != " ":
                    stack.append(level[index])
            stacks.append(stack)
        return stacks

    def cratemover9000(self, procedure):
        """Move a block from one stack to another (LIFO)."""
        count, from_stack, to_stack = self._ingest_procedure(procedure)
        for _ in range(count):
            self.stacks[to_stack - 1].append(self.stacks[from_stack - 1].pop())

    def cratemover9001(self, procedure):
        """Move multiple blocks at a time from one stack to another."""
        count, from_stack, to_stack = self._ingest_procedure(procedure)
        load = reversed([self.stacks[from_stack - 1].pop() for _ in range(count)])
        self.stacks[to_stack - 1].extend(load)

    @staticmethod
    def _ingest_procedure(procedure):
        pattern = r"move (\d+) from (\d+) to (\d+)"
        match = re.match(pattern, procedure)
        count, from_stack, to_stack = map(int, match.groups())
        return count, from_stack, to_stack


def get_stack_tops(input: str, cratemover_version: str) -> str:
    """Get the top of each stack."""
    stacks_input, procedure_input = input.split("\n\n")
    shipyard = Shipyard(stacks_input)
    for procedure in procedure_input.splitlines():
        getattr(shipyard, cratemover_version)(procedure)
    return "".join(stack[-1] for stack in shipyard.stacks)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file, "r", encoding="utf-8") as f:
        input = f.read()
    print("Part 1:", get_stack_tops(input, "cratemover9000"))
    print("Part 2:", get_stack_tops(input, "cratemover9001"))
