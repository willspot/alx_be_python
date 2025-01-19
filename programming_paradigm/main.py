# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    # Ensure there are exactly 3 command-line arguments: script name, numerator, and denominator
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Retrieve the numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
