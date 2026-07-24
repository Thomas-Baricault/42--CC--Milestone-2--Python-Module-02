#!/usr/bin/python3

def check_temperature(temp_str: str) -> int:
    """Check if the temperature is a valid temperature

    A valid temperature is a number between 0 and 40

    Parameters
    ----------
    temp_str : str
        The temperature in °C

    Returns
    -------
    int
        The converted temperature if valid, None otherwise
    """

    try:
        temp_int = int(temp_str)
        if temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        elif temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
            return temp_int
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """Test multiple values as temperatures"""

    for test in ["25", "abc", "100", "-50"]:
        print(f"Testing temperature: {test}")
        check_temperature(test)
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature_input()
    print("All tests completed - program didn't crash!")
