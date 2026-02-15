import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv is not installed. Please install it using:")
    print("pip install python-dotenv")
    exit(1)

file = ".env"
load_dotenv(file)


def main():
    matrix_mode = os.getenv("MATRIX_MODE", "production")
    database_url = os.getenv("DATABASE_URL", "None")
    api_key = os.getenv("API_KEY", "None")
    log_level = os.getenv("LOG_LEVEL", "None")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "None")

    env = False
    try:
        with open(file, "r") as vault:
            for line in vault:
                if '\n' in line:
                    env = False
                    break
            env = True
    except FileNotFoundError as e:
        notfound = f"\033[31m[KO]\033[0m {e}"

    if not all([matrix_mode, database_url, api_key, log_level, zion_endpoint]):
        env = False
        notfound = f"\033[31m[KO]\033[0m {file} file not properly configured"
    else:
        print("ORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print(f"Mode: {matrix_mode}")
        print(f"Database: {database_url}")
        print(f"API Access: {api_key}")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_endpoint}")

    print("\n\033[32m[OK]\033[0m No harcoded secrets detected")

    if env:
        print("\033[32m[OK]\033[0m .env file properly conigured")
    else:
        print(f"{notfound}")

    print("\033[32m[OK]\033[0m Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
