"""Module for tracking and analyzing player achievements
using set operations."""


def main() -> None:
    """
    Perform analytics on player achievements using set theory.

    Calculates unique, common, solo, and rare achievements across multiple
    players to demonstrate set unions, intersections, and differences.
    """
    print("=== Achievement Tracker System ===\n")

    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "level_10", "treasure_hunter", "boss_slayer",
                   "speed_demon", "perfectionist"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    # Common achievements
    common = alice.intersection(bob.intersection(charlie))
    print(f"\nCommon to all players {common}")

    # Solo achievements
    solo_alice = alice - bob - charlie
    solo_bob = bob - alice - charlie
    solo_charlie = charlie - bob - alice

    # Rare achievements
    rare = solo_alice.difference(solo_charlie, solo_bob)

    print(f"Rare achievements (1 player): {rare}")

    alice_and_bob = alice.intersection(bob)
    alice_difference = alice.difference(bob)
    bob_difference = bob.difference(alice)
    print(f"\nAlice vs Bob common: {alice_and_bob}")
    print(f"Alice unique: {alice_difference}")
    print(f"Bob unique: {bob_difference}")


if __name__ == "__main__":
    main()
