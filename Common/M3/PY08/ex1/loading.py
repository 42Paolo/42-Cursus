import sys
import pandas as pd
import numpy as np
import requests
import matplotlib as mpl

print()
print("LOADING STATUS: Loading programs...")
print()
print("Checking dependencies:")

if "sys" not in sys.modules:
    print("[ERR] sys - Core module not ready")
else:
    print("[OK] sys - Core module ready")

if "pd" not in sys.modules:
    print("[ERR] pandas - Data manipulation not ready")
else:
    print("[OK] pandas", pd.__version__, "- Data manipulation ready")

if "np" not in sys.modules:
    print("[ERR] numpy - Numerical computation not ready")
else:
    print("[OK] numpy", np.__version__, "- Numerical computation ready")

if "requests" not in sys.modules:
    print("[ERR] requests - Network access not ready")
else:
    print("[OK] requests", requests.__version__, "- Network access ready")

if "mpl" not in sys.modules:
    print("[ERR] matplotlib - Plotting not ready")
else:
    print("[OK] matplotlib", mpl.__version__, "- Visualization ready")