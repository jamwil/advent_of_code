"""Day 6 of the Advent of Code."""


from pathlib import Path


def subroutine(buffer, distinct_chars):
    """Subroutine."""
    for ix in range(distinct_chars, len(buffer)):
        marker = set(buffer[ix - distinct_chars : ix])
        if len(marker) == distinct_chars:
            return ix
    raise ValueError("No solution found.")


if __name__ == "__main__":
    file_input = Path(__file__).parent / "input.txt"
    with open(file_input, "r", encoding="utf-8") as file:
        buffer_stream = file.read().strip()
    print(subroutine(buffer_stream, 4), subroutine(buffer_stream, 14))
