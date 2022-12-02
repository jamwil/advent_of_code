"""Day 2 of Advent of Code 2022."""


class Rock:
    """Rock tool."""

    @staticmethod
    def beats():
        return Scissors


class Paper:
    """Paper tool."""

    @staticmethod
    def beats():
        return Rock


class Scissors:
    """Scissors tool."""

    @staticmethod
    def beats():
        return Paper


CODES = {
    "A": Rock,
    "B": Paper,
    "C": Scissors,
    "X": Rock,
    "Y": Paper,
    "Z": Scissors,
}

NEEDED_OUTCOMES = {
    "X": "lost",
    "Y": "draw",
    "Z": "won",
}

TOOL_SCORING = {
    Rock: 1,
    Paper: 2,
    Scissors: 3,
}

OUTCOME_SCORING = {
    "lost": 0,
    "draw": 3,
    "won": 6,
}


def calculate_score_1(strategy_guide: str) -> int:
    """Play a game of Rock, Paper, Scissors where column B is the player choice."""
    total_score = 0
    for line in strategy_guide.splitlines():
        opponent_choice, player_choice = (CODES.get(x) for x in line.split())

        # Get the outcome of the round.
        if player_choice.beats() == opponent_choice:
            outcome = "won"
        elif player_choice == opponent_choice:
            outcome = "draw"
        else:
            outcome = "lost"
        outcome_score = OUTCOME_SCORING.get(outcome)

        # Get the tool score.
        tool_score = TOOL_SCORING.get(player_choice)

        # Add the scores together.
        total_score += outcome_score + tool_score

    return total_score


def calculate_score_2(strategy_guide: str) -> int:
    """Play a game of Rock, Paper, Scissors where column B is the needed outcome."""
    total_score = 0
    for line in strategy_guide.splitlines():
        opponent_choice, needed_outcome = line.split()
        opponent_choice = CODES.get(opponent_choice)
        needed_outcome = NEEDED_OUTCOMES.get(needed_outcome)

        # Get the outcome of the round.
        outcome_score = OUTCOME_SCORING.get(needed_outcome)

        # Determine which tool to play
        if needed_outcome == "lost":
            player_choice = opponent_choice.beats()
        elif needed_outcome == "draw":
            player_choice = opponent_choice
        else:
            player_choice = opponent_choice.beats().beats()

        # Get the tool score.
        tool_score = TOOL_SCORING.get(player_choice)

        # Add the scores together.
        total_score += outcome_score + tool_score

    return total_score


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print("Part 1:", calculate_score_1(data))
    print("Part 2:", calculate_score_2(data))
