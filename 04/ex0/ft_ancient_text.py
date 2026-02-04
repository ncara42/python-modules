"""Docstrings"""


def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        vault = open("ancient_fragment.txt", "r")
        print("\nAccesing Storage Vault: ancient_fragment.txt")
        print("Connection established...")

        print("\nRECOVERED DATA")
        print(vault.read())
        vault.close()
        
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data_generator.py first.")


if __name__ == "__main__":
    main()
