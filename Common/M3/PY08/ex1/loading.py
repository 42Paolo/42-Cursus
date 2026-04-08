import sys

try:
    import pandas as pd
    import numpy as np
    import requests
    import matplotlib as mpl
    from matplotlib import pyplot as plt
except ImportError:
    pass

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
    print(f"[OK] pandas {pd.__version__} - Data manipulation ready")

if "np" not in sys.modules:
    print("[ERR] numpy - Numerical computation not ready")
else:
    print(f"[OK] numpy {np.__version__} - Numerical computation ready")

if "requests" not in sys.modules:
    print("[ERR] requests - Network access not ready")
else:
    r_ver = requests.__version__
    print(f"[OK] requests {r_ver} - Network access ready")

if "mpl" not in sys.modules:
    print("[ERR] matplotlib - Plotting not ready")
else:
    m_ver = mpl.__version__
    print(f"[OK] matplotlib {m_ver} - Visualization ready")

if "pd" in sys.modules and "np" in sys.modules and "mpl" in sys.modules:
    print("\nAnalyzing Matrix data...")
    
    data = np.random.rand(1000, 2)
    print("Processing 1000 data points...")
    
    df = pd.DataFrame(data, columns=['Vector A', 'Vector B'])
    
    print("Generating visualization...")
    df.plot()
    plt.title("Matrix Analysis Output")
    plt.savefig('matrix_analysis.png')
    
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
else:
    print("\n[!] Errore: dipendenze mancanti.")
    print("Installa con: pip install -r requirements.txt O poetry install")
    sys.exit(1)

print("\n--- PIP vs POETRY ---")
print("PIP: usa requirements.txt, installazione flat, meno controllo versioni.")
print("POETRY: usa pyproject.toml, gestione isolata e lock file deterministico.")