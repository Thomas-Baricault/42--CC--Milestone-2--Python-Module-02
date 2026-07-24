#!/usr/bin/python3

class GardenError(Exception):
    """Exception raised for garden errors"""

    def __init__(self, message: str) -> None:
        """
        Parameters
        ----------
        message : str
            The error message
        """

        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for plant errors"""

    def __init__(self, plant: str) -> None:
        """
        Parameters
        ----------
        plant : str
            The plant name
        """

        super().__init__(f"The {plant} plant is wilting!")


class WaterError(GardenError):
    """Exception raised for water errors"""

    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def test_plant_error() -> None:
    """Test the PlantError exception"""

    print("Testing PlantError...")
    try:
        raise PlantError("tomato")
    except PlantError as e:
        print("Caught PlantError:", e)
    print()


def test_water_error() -> None:
    """Test the WaterError exception"""

    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print("Caught WaterError:", e)
    print()


def test_all_errors() -> None:
    """Test all the garden errors exceptions"""

    print("Testing catching all garden errors...")
    try:
        raise PlantError("tomato")
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        raise WaterError()
    except GardenError as e:
        print("Caught a garden error:", e)
    print()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_plant_error()
    test_water_error()
    test_all_errors()
    print("All custom error types work correctly!")
