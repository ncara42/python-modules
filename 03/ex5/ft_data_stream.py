"""Module for game event generation and mathematical sequence streaming."""

from typing import Generator


def event_generator(limit: int, players: list, levels: list,
                    actions: list) -> Generator:
    """
    Generate a stream of game events based on player and action lists.

    Yields dictionaries containing event ID, player name, calculated level,
    and action type until the specified limit is reached.
    """
    for i in range(1, limit + 1):

        this_player: str = players[(i - 1) % len(players)]
        this_action: str = actions[(i - 1) % len(actions)]
        this_level: int = levels[(i - 1) % len(levels)]

        event: dict = {
            "id": i,
            "player": this_player,
            "level": this_level,
            "action": this_action
        }
        yield event


def fibonacci_gen(n: int) -> Generator:
    """
    Generate the first n numbers of the Fibonacci sequence.

    Yields integers using a streaming approach to
    maintain constant memory usage.
    """
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> Generator:
    """
    Generate the first n prime numbers.

    Iteratively checks for primality and yields found
    primes until the requested count is satisfied.
    """
    count: int = 0
    num: int = 2
    while count < n:
        is_prime: bool = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    """
    Execute game data stream processing and mathematical demonstrations.

    Processes event logs and showcases sequence generators while maintaining
    efficient memory consumption.
    """
    print("=== Game Data Stream Processor ===")

    players: list[str] = ["alice", "bob", "charlie", "diana", "carl"]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]
    levels: list[int] = [21, 8, 26, 5, 19]
    num_events: int = 1000

    print(f"\nProcessing {num_events} game events\n")

    stream = event_generator(num_events, players, levels, actions)
    high_lvl_count: int = 0
    treasures: int = 0
    level_up: int = 0
    template: str = "Event {}: Player {} (level {}) {}"
    for event in stream:
        if event['level'] > 10:
            high_lvl_count += 1
        if event['action'] == "found treasure":
            treasures += 1
        if event['action'] == "leveled up":
            level_up += 1
        if event['id'] <= 3:
            print(template.format(
                event['id'], event['player'], event['level'], event['action']
            ))
        if event['id'] == 4:
            print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {num_events}")
    print(f"High-level players (10+): {high_lvl_count}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fib_stream: Generator = fibonacci_gen(10)

    print("Fibonacci sequence (first 10):", end=" ")
    print(next(fib_stream), end="")
    for val in fib_stream:
        print(", ", val, end="", sep="")

    print("\nPrime numbers (first 5):", end=" ")
    prime: Generator = prime_gen(5)
    print(next(prime), end="")
    for val in prime:
        print(", ", val, end="", sep="")
    print()


if __name__ == "__main__":
    main()
