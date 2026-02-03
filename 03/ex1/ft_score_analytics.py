"""Docstring"""


import sys

def main() -> None:
    print("=== Player Score Analytics ===")
    total_args = len(sys.argv)
    if total_args == 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        scores = []
        try:
            for score in sys.argv[1:]:
                number = int(score)
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
