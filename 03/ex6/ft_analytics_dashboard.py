"""Module for game analytics and comprehension demonstrations."""


def main() -> None:
    """Execute analytics dashboard using various Python comprehensions."""
    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    players: dict[str, dict[str, int | bool]] = {
        "alice": {"score": 2300, "achievements": 5, "active": True},
        "bob": {"score": 1800, "achievements": 3, "active": True},
        "charlie": {"score": 2150, "achievements": 7, "active": True},
        "diana": {"score": 2050, "achievements": 4, "active": False}
    }

    achievements = ["first_kill", "level_10", "boss_slayer", "first_kill"]
    regions = ["north", "east", "central"]

    high_scorers = [n for n, i in players.items() if i['score'] > 2000]
    doubled = [i['score'] * 2 for i in players.values()]
    active_players = [p for p, i in players.items() if i['active']]

    print(f"High scores (>2000) {high_scorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    scores = {n: i['score'] for n, i in players.items()}
    level = {
        n: "pro" if i['score'] > 2100 else "noob"
        for n, i in players.items()
    }
    num_achievs = {n: i['achievements'] for n, i in players.items()}

    print(f"Player scores: {scores}")
    print(f"Score categories: {level}")
    print(f"achievement counts: {num_achievs}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {a for a in players}
    unique_achievements = {a for a in achievements}
    active_regions = {a for a in regions}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    score_list = [av['score'] for av in players.values()]
    template: str = "Top performer: {} ({} points, {} achievements)"
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {sum(score_list) / len(players)}")
    top = max(players, key=lambda name: players[name]['score'])
    print(template.format(
        top, players[top]['score'], players[top]['achievements']
    ))


if __name__ == "__main__":
    main()
