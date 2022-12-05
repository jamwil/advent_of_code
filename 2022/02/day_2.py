"""Day 2 of Advent of Code 2022."""
from enum import Enum
from pathlib import Path


class Rock:
    """Rock tool."""

    tool_score = 1

    @staticmethod
    def beats():
        return Scissors


class Paper:
    """Paper tool."""

    tool_score = 2

    @staticmethod
    def beats():
        return Rock


class Scissors:
    """Scissors tool."""

    tool_score = 3

    @staticmethod
    def beats():
        return Paper


class Outcomes(Enum):
    """Outcome of a round."""

    won = 6
    draw = 3
    lost = 0


CODES = {
    "A": Rock,
    "B": Paper,
    "C": Scissors,
    "X": Rock,
    "Y": Paper,
    "Z": Scissors,
}

NEEDED_OUTCOMES = {
    "X": Outcomes.lost,
    "Y": Outcomes.draw,
    "Z": Outcomes.won,
}


def calculate_score_1(strategy_guide):
    """Play a game of Rock, Paper, Scissors where column B is the player choice."""
    total_score = 0
    for line in strategy_guide.splitlines():
        opponent_choice, player_choice = (CODES.get(x) for x in line.split())

        if player_choice.beats() == opponent_choice:
            outcome = Outcomes.won
        elif player_choice == opponent_choice:
            outcome = Outcomes.draw
        else:
            outcome = Outcomes.lost

        total_score += outcome.value + player_choice.tool_score

    return total_score


def calculate_score_2(strategy_guide):
    """Play a game of Rock, Paper, Scissors where column B is the needed outcome."""
    total_score = 0
    for line in strategy_guide.splitlines():
        opponent_choice, needed_outcome = line.split()
        opponent_choice = CODES.get(opponent_choice)
        needed_outcome = NEEDED_OUTCOMES.get(needed_outcome)

        if needed_outcome == Outcomes.lost:
            player_choice = opponent_choice.beats()
        elif needed_outcome == Outcomes.draw:
            player_choice = opponent_choice
        else:
            player_choice = opponent_choice.beats().beats()

        total_score += needed_outcome.value + player_choice.tool_score

    return total_score


if __name__ == "__main__":
    input_data = Path(__file__).parent.resolve() / "input.txt"
    with open(input_data, "r", encoding="utf-8") as file:
        data = file.read()
    print("Part 1:", calculate_score_1(data))
    print("Part 2:", calculate_score_2(data))
