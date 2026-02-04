"""Docstrings"""

def main() -> None:
    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    players = {

        "alice": {"score": 2300, "achievements": 5, "active": True},
        "bob": {"score": 1800, "achievements": 3, "active": True},
        "charlie": {"score": 2150, "achievements": 7, "active": True},
        "diana": {"score": 2050, "achievements": 4, "active": False}
    }

    achievements = ["first_kill", "level_10", "boss_slayer", "first_kill"]
    regions = ["north", "east", "central"]

    high_scorers = [name for name, info in players.items() if info['score'] > 2000]
    doubled = [info['score'] * 2 for info in players.values()]
    active = [active for active, info in players.items() if info['active'] == True]

    print(f"High scores (>2000) {high_scorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    scores = {name: info['score'] for name, info in players.items()}
    level = {name: "pro" if info['score'] > 2100 else "noob" for name, info in players.items()}
    number_achievements = {name: info['achievements'] for name, info in players.items()}

    print(f"Player scores: {scores}")
    print(f"Score caregories: {level}")
    print(f"achievement counts: {number_achievements}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = sorted(set(players))
    unique_achievements = set(achievements)
    active_regions = set(regions)
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    average_score = [av['score'] for av in players.values()]
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(achievements)}")
    print(f"Average score: {sum(average_score) / len(players)}")
    top = max(players, key=lambda name: players[name]['score'])
    print(f"Top performer: {top} ({players[top]['score']} points, {players[top]['achievements']} achievements)")


if __name__ == "__main__":
    main()