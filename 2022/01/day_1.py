"""Find the elf carrying the most calories."""
from pathlib import Path


def main():
    """Find the elf carrying the most calories."""
    input_data = Path(__file__).parent.resolve() / "input.txt"
    with open(input_data, "r", encoding="utf-8") as file_handle:
        lines = file_handle.readlines()
    elves = [0]
    for line in lines:
        if line == "\n":
            elves.append(0)
        else:
            elves[-1] += int(line)
    elves.sort(reverse=True)
    print("Calories of fattest elf:", elves[0])
    print("Calories of top 3 fattest elves:", sum(elves[:3]))


if __name__ == "__main__":
    main()
