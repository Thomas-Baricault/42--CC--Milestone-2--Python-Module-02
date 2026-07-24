#!/usr/bin/python3

def garden_operations() -> None:
    """Raise multiple types of errors"""

    int("abc")
    73 / 0
    open("missing.txt")
    {73: "abc"}["missing_plant"]


def test_error_types() -> None:
    """Test multiple types of errors and catch them all"""

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print("Caught ValueError:", e)
    print()
    print("Testing ZeroDivisionError...")
    try:
        73 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print()
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    print()
    print("Testing KeyError...")
    try:
        {73: "abc"}["missing_plant"]
    except KeyError as e:
        print("Caught KeyError:", e)
    print()
    print("Testing multiple errors together...")
    try:
        garden_operations()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but the program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    # garden_operations()
    test_error_types()
