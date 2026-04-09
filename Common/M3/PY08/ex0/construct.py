import sys
import os
import site


def check_matrix():
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")

        venv_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        try:
            site_packages = site.getsitepackages()[0]
        except Exception:
            site_packages = "Unknown"

        print("Package installation path:")
        print(site_packages)
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        # Gestione stringa lunga per evitare errori E501
        instructions = (
            "The machines can see everything you install.\n"
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "Then run this program again."
        )
        print(instructions)


if __name__ == "__main__":
    check_matrix()
