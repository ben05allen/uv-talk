import cowsay
import sys


def main():
    python_version = sys.version.split()[0]
    cowsay.cow(f"Running python: {python_version}")


if __name__ == "__main__":
    main()
