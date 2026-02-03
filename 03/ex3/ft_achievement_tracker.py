"""Docstrings"""


def main():
    print("=== Achievement Tracker System ===\n")

    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achivement Analytics ===")
    
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    # Common achievements
    common = alice.intersection(bob.union(charlie))

    # Solo achievements
    solo_alice = alice.difference(bob.union(charlie))
    solo_bob = bob.difference(alice.union(charlie))
    solo_charlie = charlie.difference(alice.union(bob))
    
    # Rare achievements
    rare = solo_alice.union(solo_bob).union(solo_charlie)

    print(f"\nCommon to all players {common}")
    print(f"Rare achievements (1 player): {rare}")

    alice_and_bob = alice.intersection(bob)
    alice_difference = alice.difference(bob)
    bob_difference = bob.difference(alice)
    print(f"\nAlice vs Bob common: {alice_and_bob}")
    print(f"Alice unique: {alice_difference}")
    print(f"Bob unique: {bob_difference}")

if __name__ == "__main__":
    main()
