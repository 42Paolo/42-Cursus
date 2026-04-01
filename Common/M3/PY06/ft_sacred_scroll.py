import alchemy
import alchemy.elements

print("=== Sacred Scroll Mastery ===")

print("Testing direct module access:")
try:
    print("alchemy.elements.create_fire(): ", end='')
    print(f"{alchemy.elements.create_fire()}")
except Exception:
    print("[ERROR] - Import Error")
try:
    print("alchemy.elements.create_water(): ", end='')
    print(f"{alchemy.elements.create_water()}")
except Exception:
    print("[ERROR] - Import Error")
try:
    print("alchemy.elements.create_earth(): ", end='')
    print(f"{alchemy.elements.create_earth()}")
except Exception:
    print("[ERROR] - Import Error")
try:
    print("alchemy.elements.create_air(): ", end='')
    print(f"{alchemy.elements.create_air()}")
except Exception:
    print("[ERROR] - Import Error")

print()

print("Testing package-level access (controlled by __init__.py):")
try:
    print("alchemy.create_fire(): ", end='')
    print(f"{alchemy.create_fire()}")
except Exception:
    print("AttributeError - not exposed")

try:
    print("alchemy.create_water(): ", end='')
    print(f"{alchemy.create_water()}")
except Exception:
    print("AttributeError - not exposed")

try:
    print("alchemy.create_earth(): ", end='')
    print(f"{alchemy.create_earth()}")
except Exception:
    print("AttributeError - not exposed")

try:
    print("alchemy.create_air(): ", end='')
    print(f"{alchemy.create_air()}")
except Exception:
    print("AttributeError - not exposed")

print("\nPackage metadata: ")
print(f"Version: {alchemy.__version__}")
print(f"Author : {alchemy.__author__}")
