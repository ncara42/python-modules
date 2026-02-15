"""Module for processing and analyzing player score data
from command-line arguments"""

import sys


def main() -> None:
    """
    Calculate and display player score statistics from terminal input.

    Parses command-line arguments into integers and computes sum,
    average, high/low scores, and range.
    """
    print("=== Player Score Analytics ===")
    total_args: int = len(sys.argv)
    if total_args == 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              f"<score1> <score2> ...")
    else:
        scores: list[int] = []
        try:
            for score in sys.argv[1:]:
                number: int = int(score)
                scores += [number]
        except ValueError as e:
            print(f"{type(e).__name__}: {e}")
            return
        if scores:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores):.1f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
