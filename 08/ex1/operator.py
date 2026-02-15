"""
This script checks for the availability of specific Python dependencies
and performs a matrix data analysis.
It generates a visualization of the analysis and saves it as an image file.
"""

import importlib


def analyze_and_visualize():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests
    """
    Performs matrix data analysis and generates a visualization.

    The function creates a DataFrame with x values ranging from
    0 to 2 and their corresponding sine values.
    It calculates the square of the sine values, plots both
    the sine and squared sine values, and saves the plot
    as an image file named 'matrix_analysis.png'.
    """
    print("\nFetching Matrix data from API (simulated)...")
    # Simulation with request
    try:
        response = requests.get("https://httpbin.org/json")
        if response.status_code == 200:
            print("Data fetched successfully with requests!")
        else:
            print(f"Warning: Received status code "
                  f"{response.status_code} from API.")
    except Exception as e:
        print(f"Warning: Could not fetch data from API. Reason: {e}")

    # Using pandas, matplotlib y numpy
    print("\nAnalyzing Matrix data...")
    data = pd.DataFrame({
        "x": np.linspace(0, 10, 2000),
        "y": np.sin(np.linspace(0, 10, 2000))
    })

    print("Processing 1000 data points...")
    data["y_squared"] = data["y"] ** 2

    print("Generating visualization...")
    plt.plot(data["x"], data["y"], label="sin(x)")
    plt.plot(data["x"], data["y_squared"], label="sin(x)^2")
    plt.legend()
    plt.title("Matrix Data Analysis")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    output = "matrix_analysis.png"
    plt.savefig(output)
    print("\nAnalysis complete!")
    print(f"Results saved to: {output}")


def main():
    """
    Checks the availability of required Python
    dependencies and prints their status.
    """
    dependencies = ["pandas", "requests", "matplotlib", "numpy"]
    all_ok = True
    print("OPERATOR STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for dep in dependencies:
        try:
            module = importlib.import_module(dep)
            version = getattr(module, "__version__", "Unknown")
            print(f"\033[32m[OK]\033[0m {dep} ({version}) - Ready")
        except ImportError:
            print(f"\033[31m[KO]\033[0m {dep} - Not ready")
            all_ok = False

    if all_ok:
        analyze_and_visualize()
    else:
        print("\n\033[31mERROR\033[0m: Some dependencies are missing!")
        print("\nHow to install dependencies? Comparison:")
        print("pip:")
        print("  - Uses requirements.txt to list dependencies.")
        print("  - Install with: pip install -r requirements.txt")
        print("  - Manual version management; no lock file by default.")
        print("Poetry:")
        print("  - Uses pyproject.toml for dependencies and project metadata.")
        print("  - Install with: poetry install")
        print("  - Handles virtual environments and generates "
              "poetry.lock for reproducibility.\n")


if __name__ == "__main__":
    main()
