"""Module for managing triple-channel archive communications"""


import sys


def main():
    """
    Handles archivist status reporting.
    
    Processes user input and demonstrates communication via standard input, 
    standard output, and standard error streams.
    """
    print("=== CYBER ARCHIVES - COMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    sys.stdout.write("\n{[}STANDARD{]} Archive status from "
                     f" {archivist_id}: {status_report}\n")
    sys.stderr.write("{[}ALERT{]} System diagnostic: "
                     "Comunication channels verified\n")
    sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")

    sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    main()
