#!/usr/bin/python3

class Plant:
    """Representation of a plant

    Attributs
    ---------
    name : str
        The name of the plant
    water_level : int
        The level of water of the plant
    sunlight_hours : int
        The number of hours of sunlight the plant is exposed to

    Methods
    -------
    check_healthy() -> None
        Raises an error if the plant isn't healthy
    """

    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the plant
        water_level : int
            The level of water of the plant
        sunlight_hours : int
            The number of hours of sunlight the plant is exposed to
        """

        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours

    def check_healthy(self) -> None:
        """Raises an error if the plant isn't healthy"""

        if self.water_level < 1:
            raise Exception(f"Water level {self.water_level} is too low (min 1"
                            + ")")
        if self.water_level > 10:
            raise Exception(f"Water level {self.water_level} is too high (max "
                            + "10)")
        if self.sunlight_hours < 2:
            raise Exception(f"Sunlight hours {self.sunlight_hours} is too low "
                            + "(min 2)")
        if self.sunlight_hours > 12:
            raise Exception(f"Sunlight hours {self.sunlight_hours} is too high"
                            + " (max 12)")


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


class GardenManager:
    """A class to manage garden

    Methods
    -------
    refill(water) -> None
        Refills the tank with a quantity of water
    plant(*args) -> None
        Plant plants in the garden
    water() -> None
        Water the plants in the garden
    check_health() -> None
        Check if all the plants are healthy
    """

    def __init__(self) -> None:
        self.__tank = 0
        self.__plants: list[Plant] = []

    def refill(self, water: int) -> None:
        """Refills the tank with a quantity of water

        Parameters
        ----------
        water : int
            The quantity of water
        """

        self.__tank += water

    def plant(self, *args: Plant) -> None:
        """Plant plants in the garden

        Parameters
        ----------
        args : tuple[Plant, ...]
            The plants
        """

        print("Adding plants to garden...")
        for plant in args:
            if plant.name == "":
                raise Exception("Plant name cannot be empty!")
            self.__plants.append(plant)
            print(f"Added {plant.name} successfully")

    def water(self) -> None:
        """Water the plants in the garden"""

        if self.__tank == 0:
            raise GardenError("Not enought water in tank")
        try:
            print("Watering plants...")
            print("Opening watering system")
            for plant in self.__plants:
                if self.__tank == 0:
                    raise GardenError("Not enought water in tank")
                self.__tank -= 1
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """Check if all the plants are healthy"""

        print("Checking plant health...")
        for plant in self.__plants:
            try:
                plant.check_healthy()
                print(f"{plant.name}: healthy (water: {plant.water_level}, " +
                      f"sun: {plant.sunlight_hours})")
            except Exception as e:
                print(f"Error checking {plant.name}:", e)


if __name__ == "__main__":
    print("=== Garden Management System ===")
    print()
    manager = GardenManager()
    manager.refill(2)
    try:
        manager.plant(
            Plant("tomato", 4, 8),
            Plant("lettuce", 14, 5),
            Plant("", 7, 3),
            Plant("carrots", 7, 3)
        )
    except Exception as e:
        print("Error adding plant:", e)
    print()
    try:
        manager.water()
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")
    print()
    try:
        manager.check_health()
    except Exception as e:
        print(e)
    print()
    print("Testing error recovery...")
    try:
        manager.water()
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")
