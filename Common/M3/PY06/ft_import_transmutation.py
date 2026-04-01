
print("=== Import Transmutation Mastery ===")

if __name__ == "__main__":
    print("\nMethod 1 - Full module import:")
    try:
        import alchemy.elements
        print(
            "alchemy.elements.create_fire(): " +
            f"{alchemy.elements.create_fire()}"
            )
    except Exception as e:
        print(f"ERROR: {e}")

    print("\nMethod 2 - Specific function import:")
    try:
        from alchemy.elements import create_water
        print(f"create_water(): {create_water()}")
    except Exception as e:
        print(f"ERROR: {e}")

    print("\nMethod 3 - Aliased import:")
    try:
        from alchemy.potions import healing_potion as heal
        print(f"heal(): {heal()}")
    except Exception as e:
        print(f"ERROR: {e}")

    print("\nMethod 4 - Multiple imports:")
    try:
        from alchemy.elements import create_fire, create_earth
        from alchemy.potions import strength_potion
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength_potion()}")
    except Exception as e:
        print(f"ERROR: {e}")
    print("\nAll import transmutation methods mastered!")
