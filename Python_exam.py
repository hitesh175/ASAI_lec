"""Load example configuration without displaying secret values."""
import os
from pathlib import Path

from dotenv import load_dotenv


def main():
    load_dotenv(Path(__file__).resolve().with_name(".env"))
    required = ("MAIN_KEY", "SECRET_KEY")
    missing = [name for name in required if not os.getenv(name, "").strip()]
    if missing:
        print("Missing configuration: " + ", ".join(missing))
        return 1
    print("Keys loaded successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
