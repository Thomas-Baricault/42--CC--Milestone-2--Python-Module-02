#!/usr/bin/python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Check is a plant is healthy

    Parameters
    ----------
    plant_name : str
        The plant name
    water_level : int
        The water level (must be between 1 and 10)
    sunligh_hours : int
        The sunlight hours (must be between 2 and 12)

    Raises
    ------
    ValueError
        If plant_name is empty or if water_level or sunlight_hours aren't in a
        valid interval
    """

    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max"
                         + " 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """Try different health check to desmonstrate the differents possible
    errors"""

    print("Testing good values...")
    try:
        check_plant_health("tomato", 7, 3)
    except ValueError as e:
        print("Error:", e)
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 7, 3)
    except ValueError as e:
        print("Error:", e)
    print()
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 3)
    except ValueError as e:
        print("Error:", e)
    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 7, 0)
    except ValueError as e:
        print("Error:", e)
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    print()
    test_plant_checks()
