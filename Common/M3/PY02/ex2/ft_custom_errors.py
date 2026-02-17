class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

def raise_custom_errors() -> None:
    water_tank: int = -2
    plant_status: str = "wilting"
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError . . .")
    try:
        if plant_status == "wilting":
            raise PlantError(
                            "Caught PlantError: " +
                            "The tomato plant is wilting!\n"
            )
    except PlantError as pe:
        print(f"{pe}")

    print("Testing WaterError . . .")
    try:
        if water_tank < 0:
            raise WaterError(
                "Caught WaterError: " +
                "Not enough water in the tank!\n"
            )
    except WaterError as we:
        print(f"{we}")
    print("Testing catching all garden errors...")

    try:
        if water_tank < 0:
            raise WaterError(
                "Caught a garden error: " +
                "Not enough water in the tank!"
            )
    except GardenError as garden_error:
        print(f"{garden_error}")

    try:
        if plant_status == "wilting":
            raise PlantError(
                "Caught a garden error: " +
                "The tomato plant is wilting!\n"
            )
    except GardenError as garden_error:
        print(f"{garden_error}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    raise_custom_errors()