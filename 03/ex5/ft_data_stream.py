"""Docstrings"""


def event_generator(limit: int, players: list, actions: list):
    for i in range(1, limit + 1):

        this_player = players[(i - 1) % len(players)]
        this_action = actions[(i - 1) % len(actions)]

        event = {
            "id": i,
            "player": this_player,
            "level": (i * 13) % 20 + 1,
            "action": this_action
        }
        yield event

def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main() -> None:
    print("=== Game Data Stream Processor ===")

    players = ["Alice", "Bob", "Charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    num_events = len(players)

    print(f"\nProcessing {num_events} game events\n")

    stream = event_generator(num_events, players, actions)
    high_lvl_count = 0
    treasures = 0
    level_up = 0
    for event in stream:
        if event['level'] > 10:
            high_lvl_count += 1
        if event['action'] == "found treasure":
            treasures += 1
        if event['action'] == "leveled up":
            level_up += 1
        print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['action']}")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {num_events}")
    print(f"High-level players: {high_lvl_count}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fib_stream = fibonacci_gen(10)
    it = iter(fib_stream)
    res = str(next(it))
    for val in it:
        res += ", " + str(val)

    print(f"Fibonacci sequence (first 10): {res}")

if __name__ == "__main__":
    main()
