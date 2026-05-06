import sys

try:
    import pandas as pd
except ImportError:
    pass

try:
    import numpy as np
except ImportError:
    pass

try:
    import requests
except ImportError:
    pass

try:
    import matplotlib as mpl
    from matplotlib import pyplot as plt
except ImportError:
    pass

print("LOADING STATUS: Loading programs...")
print()
print("Checking dependencies:")

if "pandas" not in sys.modules:
    print("[ERR] pandas - Data manipulation not ready")
else:
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")

if "numpy" not in sys.modules:
    print("[ERR] numpy - Numerical computation not ready")
else:
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")

if "requests" not in sys.modules:
    print("[ERR] requests - Network access not ready")
else:
    print(f"[OK] requests ({requests.__version__}) - Network access ready")

if "matplotlib" not in sys.modules:
    print("[ERR] matplotlib - Visualization not ready")
else:
    print(f"[OK] matplotlib ({mpl.__version__}) - Visualization ready")

if ("pandas" in sys.modules
        and "numpy" in sys.modules
        and "matplotlib" in sys.modules):
    print()
    print("Analyzing Matrix data...")
    data = np.random.rand(1000, 2)
    print("Processing 1000 data points...")
    df = pd.DataFrame(data, columns=['Vector A', 'Vector B'])
    print("Generating visualization...")
    df.plot()
    plt.title("Matrix Analysis Output")
    plt.savefig('matrix_analysis.png')
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
else:
    print()
    print("[!] Missing dependencies.")
    print("Install with: pip install -r requirements.txt")
    print("           or: poetry install")
    sys.exit(1)

print()
print("--- PIP vs POETRY ---")
print("PIP: uses requirements.txt, flat installation.")
print("POETRY: uses pyproject.toml, isolation and lock file.")
