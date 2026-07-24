#!/usr/bin/python3

def water_plants(plant_list: list[str]) -> None:
    """Water a list of plants

    Parameters
    ----------
    plant_list : list[str]
        The plants to water
    """

    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Try different waterings to desmonstrate the finally block usage"""

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
