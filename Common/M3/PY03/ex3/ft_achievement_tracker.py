import sys

def main() -> None:
    print("=== Achievement Tracker System ===")
    
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    
    print("\n=== Achievement Analytics ===")
    
    all_achieve = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achieve}")
    print(f"Total unique achievements: {len(all_achieve)}")
    
    com_ach = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {com_ach}")
    
    rare_achieves = set()
    for achieve in all_achieve:
        c_achivie = 0
        if achieve in alice:
            c_achivie += 1
        if achieve in bob:
            c_achivie += 1
        if achieve in charlie:
            c_achivie += 1
        if c_achivie == 1:
            rare_achieves.add(achieve)
    
    print(f"Rare achievements (1 player): {rare_achieves}")
    
    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")
    
    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    
    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()