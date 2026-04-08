import sys
import os
import site

if __name__ == "__main__":
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
		print("""The machines can see everything you install.
	To enter the construct, run:
	python -m venv matrix_env
	source matrix_env/bin/activate # On Unix
	matrix_env\\Scripts\\activate # On Windows
	Then run this program again.""")
