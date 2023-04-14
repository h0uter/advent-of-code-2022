from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


LETTER_2_MOVE_PLAYER1 = {
    "A": Move.ROCK,
    "B": Move.PAPER,
    "C": Move.SCISSORS,
}

LETTER_2_MOVE_PLAYER2 = {
    "X": Move.ROCK,
    "Y": Move.PAPER,
    "Z": Move.SCISSORS,
}


def calc_round_score(player1_move: Move, player2_move: Move) -> int:
    if player2_move == player1_move:
        if player2_move == Move.ROCK:
            return Outcome.DRAW.value + Move.ROCK.value
        if player2_move == Move.PAPER:
            return Outcome.DRAW.value + Move.PAPER.value
        if player2_move == Move.SCISSORS:
            return Outcome.DRAW.value + Move.SCISSORS.value

    if player2_move == Move.ROCK:
        if player1_move == Move.PAPER:
            return Outcome.LOSS.value + Move.ROCK.value
        else:
            return Outcome.WIN.value + Move.ROCK.value

    if player2_move == Move.PAPER:
        if player1_move == Move.SCISSORS:
            return Outcome.LOSS.value + Move.PAPER.value
        else:
            return Outcome.WIN.value + Move.PAPER.value

    if player2_move == Move.SCISSORS:
        if player1_move == Move.ROCK:
            return Outcome.LOSS.value + Move.SCISSORS.value
        else:
            return Outcome.WIN.value + Move.SCISSORS.value


def calc_scores(filename):
    lines = open(filename).read().splitlines()

    player1_scores = []

    for line in lines:
        player1_move, player2_move = line.split(" ")
        player1_move = LETTER_2_MOVE_PLAYER1[player1_move]
        player2_move = LETTER_2_MOVE_PLAYER2[player2_move]

        player1_scores.append(calc_round_score(player1_move, player2_move))

    total_score = sum(player1_scores)
    return total_score


if __name__ == "__main__":
    # print(calc_scores("day2/debug_input.txt"))
    print(calc_scores("day2/input.txt"))
