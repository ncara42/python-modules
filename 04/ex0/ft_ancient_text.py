"""Cyber Archives data recovery module"""

def main() -> None:
    """
    Main entry point for the data recovery system.
    
    Processes the recovery of fragment data from a specified file
    and handles potential file access errors.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file = "ancient_fragment.txt"
    try:
        vault = open(file, "r")
        print(f"\nAccesing Storage Vault: {file}")
        print("Connection established...")

        print("\nRECOVERED DATA")
        print(vault.read())
        vault.close()

        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data_generator.py first.")


if __name__ == "__main__":
    main()
