import alchemy

if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    try:
        from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
        print(f"lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}")
    except Exception as e:
        print(f"ERROR: {e}")

    print("\nTesting Relative Imports (from advanced.py):")
    try:
        from alchemy.transmutation.advanced import (
            philosophers_stone,
            elixir_of_life
        )
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life(): {elixir_of_life()}")
    except Exception as e:
        print(f"ERROR: {e}")

    print("\nTesting Package Access:")
    try:
        print(
            "alchemy.transmutation.lead_to_gold(): " +
            f"{alchemy.transmutation.lead_to_gold()}"
            )
        print(
            "alchemy.transmutation.philosophers_stone(): " +
            f"{alchemy.transmutation.philosophers_stone()}"
            )
    except Exception as e:
        print(f"ERROR: {e}")

    print("Both pathways work! Absolute: clear, Relative: concise")
